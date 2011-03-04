# Module which map services to back-ends, with ability to redirect
# clients to a particular back-end node for 10 minutes at a time.
#
# The module reads an external mapping table which maps URL regexps
# to "|"-separated list of back-end hosts. Each such rule can have
# additional :attributes attached to it. The exact rule syntax is:
#
#   REGEXP HOST[|HOST]... [:ATTRIBUTE]
#
# White space in beginning and end of lines is ignored. After that
# any empty lines and lines beginning with "#" are ignored. The rest
# must be rules conforming to the syntax shown above. Apart for the
# attributes this is mostly like Apache's external rewrite map.
#
# The REGEXP specifies pattern to match against the unparsed URI.
# Normally it should be anchored to beginning: "^/dqm(?:/.*)?$".
#
# The "|"-separated list specifies back-end hosts the service will be
# sent to. One is selected in round-robin random series.
#
# If the rule has trailing :affinity attribute, then clients will be
# sent a cookie to remember the selected host. Subsequent accesses
# from the same client will use the cookie provided it is still valid.
#
# If :affinity is enabled, the mapping to back-end hosts is done with
# consistent hashing lookup: the cookie stores a hash of the previous
# server choice, and we'll keep going to the same host as long as it
# is available in the server map. If the server list changes so that
# the previous host is no longer available, the request will be sent
# to some other host instead.
#
# Hence when processing the service host list, we create a hash table
# of the host names, with 500 hashed versions of each candidate as is
# customary for consistent hashing to achieve even distribution. The
# hash list is sorted by increasing hash order by hash hex string.
#
# When looking for a match by the hash, i.e. from 'cms-node' affinity
# cookie, we scan the list of hashes for that service from beginning
# until we find a hash not less than the incoming hash, or we reach
# the end of the list. The server for that hash will satisfy this
# and future requests from the client.
#
# Usually the selected server will be the one the client used before,
# and the hashes will compare equal. If the server list changes, we
# may choose a different server. As long as previously used server
# remains on the list, it will continue to be selected by the hash.
# Either way, the same choice will be made consistently as long as
# the server list remains unchanged.
#
# The affinity cookie is has the following structure, with all the
# fields being lowercase hex characters, 88 characters in total:
# - 1..8: unix epoch timestamp when cookie was created
# - 9..48: hash for the back-end server to use
# - 49..88: sha1 hmac over 1..48 plus secret signing key
#
# Note that the cookie has a hmac which prevents clients from setting
# a valid cookie. The client cannot construct a server selection even
# if they knew which back-end host they wanted to get to. The cookie
# is only set only when needed. All processing happens as the request
# passes through, there are no extra round-trips to the client.
package cmshosts;
use strict;
use warnings;
use Apache2::ServerUtil;
use File::Spec::Functions qw(rel2abs);
use Digest::SHA1 'sha1_hex';
use Apache2::Const -compile => ':common', ':http';
use cmstools;

use constant LOCK_PERIOD => 600;
use constant HASH_DUPS => 500;
use constant DEBUG => 0;
my $backends = [];
my $reloaded = 0;

sub handler($);
sub reload_conf($);
sub choose_backend($);

# Main handler routine, hooked to every request. Re-reads the mapping
# table if more than 15 seconds have passed from last refresh. Then
# does the actual mapping logic, and finally returns DECLINED to tell
# Apache to keep on processing the request.
#
# Note that this handler may trigger several times for a single HTTP
# request, for example when authentication does internal redirects.
sub handler($)
{
  my ($r) = @_;
  my $now = $r->request_time;
  if ($now - $reloaded > 15)
  {
    reload_conf($r);
    $reloaded = $now;
  }

  choose_backend($r);
  return Apache2::Const::DECLINED;
}

# Re-read configuration. Reads both the mapping table and secret key.
sub reload_conf($)
{
  my ($r) = @_;
  my $server_root = Apache2::ServerUtil::server_root();
  my $host_map = $r->server->dir_config("HOST_MAP");

  # Check we have required variables.
  if (! $host_map)
  {
    $r->log->error("HOST_MAP required for cmshosts mapping");
    die;
  }

  if (! secret_load(map { rel2abs($_, $server_root) }
		    $r->dir_config->get("AUTH_HMAC_KEYS"))
      || ! secret_key("host-map"))
  {
    $r->log->error("AUTH_HMAC_KEYS 'host-map' key required");
    die;
  }

  # Re-read mapping table.
  my $nerr = 0;
  my $newmap = [];
  my $f = rel2abs $host_map, $server_root;
  $r->log->notice("reloading mappings from $f") if DEBUG;
  open(F, "< $f") or die "$f: $!";
  while (<F>)
  {
    # Skip empty and comment lines.
    chomp; s/^\s+//; s/\s+$//;
    next if /^#.*/ || /^$/;

    # Parse the rule; compile the rule regexp.
    if (! /^(\S+)\s+(\S+)(\s+((:\w+)(\s+:\w+)*))?$/)
    {
      $r->log->error("$f: $.: syntax error");
      ++$nerr;
      next;
    }

    my $rule = { URIRX => qr/$1/,
                 HOSTS => [split /\|/, $2],
                 ATTRS => [split /\s+/, $4 || ""],
		 HASHED => [] };

    # If we have affinity, create reverse lookup hash table.
    # Position every host HASH_DUPS times in hash-sorted order.
    if (grep /:affinity/, @{$$rule{ATTRS}})
    {
      my @hashed;
      foreach my $host (@{$$rule{HOSTS}})
      {
        push(@hashed, [sha1_hex("$host:$_"), $host]) for 1 .. HASH_DUPS;
      }

      push(@{$$rule{HASHED}}, sort { $$a[0] cmp $$b[0] } @hashed);
    }

    # Append this rule.
    push(@$newmap, $rule);

    $r->log->notice("rule: rx=$$rule{URIRX}"
		    . " hosts=(@{$$rule{HOSTS}})"
		    . " ATTRS=(@{$$rule{ATTRS}})"
		    . " #HASHED=@{[scalar @{$$rule{HASHED}}]}")
      if DEBUG;
  }
  close(F);

  # If we parsed rules successfully, remember the new rule set.
  # Otherwise keep using the old rules.
  $backends = $newmap if ! $nerr;
}

# Handle choice of a backend.
#
# Matches the URI against backend URL patterns. The first pattern to
# match defines set of hosts the request can be sent to.
#
# If the pattern has :affinity attribute, checks if the incoming
# request has a valid 'cms-node' cookie set. If so, uses the node
# hash from the cookie to select a server, using consistent hashing.
#
# Otherwise, picks server from available hosts and rotates the
# server list for round-robin server selection. If :affinity is
# enabled, adjusts outgoing headers to set a cookie so the client
# will request to come back to the same back-end node.
sub choose_backend($)
{
  my ($r) = @_;
  my $uri = $r->unparsed_uri;
  my $now = $r->request_time;
  my $backend = undef;

  # Walk over all rules, pick the first that matches the URI.
  for my $rule (@$backends)
  {
    $r->log->notice("considering $uri vs. $$rule{URIRX},"
		    . " hosts: @{$$rule{HOSTS}},"
		    . " attrs: @{$$rule{ATTRS}}")
      if DEBUG;

    next if $uri !~ /$$rule{URIRX}/;

    # See if the rule requires affinity.
    my $c;
    my $reset = 1;
    my $affinity = grep /:affinity/, @{$$rule{ATTRS}};
    my $hashed = $$rule{HASHED};

    # If affinity is requested, we have a cookie, that cookie
    # is valid, both in structure and hmac still matches, and
    # the cookie hasn't expired, honour the cookie.
    if ($affinity
        && ($c = cookie_from_header($r, 'cms-node'))
	&& $c =~ /^([0-9a-f]{8})([0-9a-f]{40})([0-9a-f]{40})$/
	&& secret_hmac_check("host-map", "$1$2", $3)
        && $now - hex($1) < LOCK_PERIOD)
    {
      # Choose right server - this is consistent hashing algo.
      my $n = scalar @$hashed;
      my $i = 0;

      ++$i while $i < $n-1 && $2 gt $$hashed[$i][0];
      $backend = $$hashed[$i][1];
      $reset = 0;

      $r->log->notice("affinity found, cookie $c, backend $backend,"
		      . " hash was $2, using $$hashed[$i][0]")
	if DEBUG;
    }

    # If we didn't settle on a backend, pick one now with
    # round-robin rotation so we distribute server load.
    if (! defined $backend)
    {
      $backend = shift(@{$$rule{HOSTS}});
      push(@{$$rule{HOSTS}}, $backend);
      $r->log->notice("choosing backend $backend") if DEBUG;
    }

    # If affinity was requested, set a cookie if we need to tell the
    # client to remember the choice. This happens if there was no
    # incoming cookie, the cookie was invalid, or had expired.
    if ($affinity && $reset)
    {
      # Find some (any) hash that matches the selected host.
      my $hash = (grep($$_[1] eq $backend, @$hashed))[0];

      # Build cookie.
      my $data = sprintf("%08x%s", time(), $$hash[0]);
      $data .= secret_hmac("host-map", $data);
      my $cookie = "cms-node=$data;path=/;secure;httponly";

      # Send cookie to client and add it to the request.
      $r->err_headers_out->add("Set-Cookie" => $cookie);
      $r->headers_in->set("Cookie" => join("; ", "cms-node=$data",
					   $r->headers_in->get("Cookie")));

      $r->log->notice("affinity, setting cookie $cookie"
		      . " for backend $backend, hash $$hash[0]")
	if DEBUG;
    }

    # We are done.
    last;
  }

  # Set backend environment variable to selected host, if any.
  $r->log->notice("final backend <" . ($backend || "(none)") . ">") if DEBUG;
  $r->subprocess_env('BACKEND' => $backend) if defined $backend;
}

1;
