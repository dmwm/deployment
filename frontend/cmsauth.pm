# CMSWEB authentication and authorisation module.
#
# This module is set up in Apache in /auth URL space. Requests to the
# protected applications are sent here as internal redirections using
# Apache rewrite engine (mod_rewrite). The module authenticates the
# client. If authentication is mandatory and the client cannot be
# verified, access is denied. Otherwise access is allowed and HTTP
# request headers are modified to report authentication information.
#
# If authentication succeeds, the users' roles are retrieved from the
# CMS authorisation database (SiteDB), although this happens via an
# intermediary JSON file so the httpd server isn't dependent on the
# database availability. If the user is known and has authorisation
# roles, the information is added to the HTTP request headers. The
# back-end apps should use the information from headers to determine
# actions applicable to the user.
#
# Any authn/authz headers present in the original HTTP request are
# always completely removed. The module adds headers based on the
# authn/authz results, and adds HMAC of the added headers so the
# back-ends can verify the integrity of the information.
#
# When a request arrives in Apache, application proxy rules should
# set AUTH_SPEC environment variable to the app authentication and
# authorisation options, and rewrite the entire URI including any
# query string to begin with /auth/verify. If authentication is
# completed, the request is rewritten to /auth/complete followed
# by the full original URI, including any query string arguments.
# The real proxy rules should be attached there. If authentication
# fails, the URI is reset to the original location and processing is
# terminated with 403 Forbidden.
#
# AUTH_SPEC should be semi-colon separated list of authentication
# options. The entries are processed in the order given, and the
# first option to satisfy the authentication is taken. If the
# module reaches the end of the list, the authentication fails.
# The possible options are:
#
#  cert
#
#   Allow accesses by X509 grid certificate or a proxy thereof. Only
#   certificates which are CMS VO members or on a special exemption
#   list of known important service certificates are accepted.
#
#  limited-proxy
#
#   Add this option to also permit limited proxies in addition to the
#   normal certificates and proxies allowed by 'cert'.
#
#  host
#
#   Allow certain hosts based on IP address exemption list. This is
#   the weakest possible authentication method and should only grant
#   viewing rights to relatively non-sensitive information. The IP
#   list maintains known CMS centre monitoring stations at various
#   locations around the world. In some cases there is no possibility
#   for a human to interact with the station, and no meaningful
#   authentication is possible.
#
#  aucookie
#
#   This method is for legacy support. The 'cert' method sets bogus
#   cookie which can later be handed back to the server without a
#   certificate. The server will know the access is valid, but does
#   not record who the access was by, so authorisation will be void.
#
#  optional
#
#   Marks the entire authentication optional, access is allowed even
#   if none of the authentication methods succeed. The application
#   must be aware that requests may come from unidentified non-CMS
#   clients. Use this if only certain parts of the application are
#   sensitive and the application performs additional protection.
#
#  authz=off
#
#   Authenticate but disable authorisation, presumably because the
#   application has no use for the information. Use this if the app
#   should be restricted to CMS users only, but does not perform any
#   meaningful actions, for example offers no modification ability.
#
#  roles=<regexp>
#
#   This option may be specified repeatedly. Each specification adds
#   a regular expression filter to include only certain roles to the
#   back-end authorisation lists. Use this to tell the application
#   only about roles the application needs to know about. The perl
#   regular expression must match the entire role string. The regexps
#   form an union: if any regexp matches, the result is included into
#   the HTTP request headers. This filter is applied before the group
#   filter.
#
#  groups=<regexp>
#
#   This option may be specified repeatedly. Each specification adds
#   a regular expression filter to include only certain groups to the
#   back-end authorisation lists. Use this to tell the application
#   only about roles and groups the application needs to know about.
#   The perl regular expression must match the entire group string.
#   The regexps form an union: if any regexp matches, the result is
#   included into the HTTP request headers. Note that site groups are
#   of the form site:name, regular groups group:name. If all groups
#   of a role are filtered out, the entire CMS-AuthZ header for that
#   role is suppressed.
#
# The module sets the following headers in the HTTP request:
#
#  CMS-Auth-Status
#
#   Presence of this header indicates the request came over SSL and
#   was authenticated. The value is "OK" if authentication succeeded,
#   "NONE" otherwise. If authentication is mandatory the value is
#   always "OK" as access is denied if the client authentication
#   fails. Hence "NONE" is possible only if the service has been
#   configured to with optional authentication.
#
#  CMS-AuthN-Method
#
#   The value of this header indicates how the client was identified,
#   as listed below. The header is present always if authentication
#   has been enabled for the application in the front-end.
#
#     X509Cert   Client used fully verified X509 grid certificate
#                and the DN is a member of CMS VO.
#
#     X509Proxy  Client used fully verified X509 grid certificate
#                proxy, whose main DN is a member of CMS VO.
#
#     X509LimitedProxy
#                Client used fully verified X509 grid certificate
#                *LIMITED* proxy, whose main DN is a member of CMS VO.
#                Applications should not necessarily grant these the
#                same powers as X509Proxy as the proxy may have been
#                harvested from a worker node. Note that this value is
#                possible only if 'limited-proxy' is active on service.
#
#     HostIP     Client IP address was exempted from authentication
#                and no stronger authentication method applied.
#
#     AUCookie   Client handed back a token from previous X509Cert
#                authentication. For legacy support only.
#
#     None       Client was not identified but authentication was
#                optional so the access was permitted.
#
#  CMS-AuthN-DN
#
#   The value of this header is the DN of the client's X509 cert. It
#   is always present when CMS-AuthN-Method is X509Cert/(Limited)Proxy.
#   This string is UTF-8.
#
#  CMS-AuthN-Login
#
#   The value of this header is the CMS hypernew login of the client.
#   It is present if CMS-AuthN-Method is X509Cert/(Limited)Proxy and 
#   SiteDB has DN account association. This string is ASCII.
#
#  CMS-AuthN-Name
#
#   The value of this header is the SiteDB registered forename and
#   surname of the client. It may not be present if the fields have
#   not been recorded in SiteDB. If authentication method is HostIP
#   or None, this header is not present. This string is UTF-8.
#
#  CMS-AuthZ-<Role>
#
#   A header for each role the client has, with space separated list
#   of group:name and site:name the role applies to. Note that all of
#   the entities -- roles, groups and sites -- are in canonical form
#   where the permitted letters are lowercase letters a-z, numbers
#   and the dash "-". All other characters are converted to "-" and
#   consecutive dashes are collapsed to one dash. This string is ASCII.
#
#  CMS-AuthN-HMAC
#
#   SHA1 HMAC over all authentication and authorisation headers. The
#   HMAC is computed from a secret key shared with back-ends and a
#   string made from all the headers and their values.
#
#   In order to compute or verify the HMAC, take all the HTTP request
#   headers, not including trailing \r\n characters, lowercase the
#   header names, and keep all headers beginning with "cms-authn" or
#   "cms-authz" except "cms-authn-hmac". Sort these headers into
#   alphabetically ascending order (a .. z) by header name.
#
#   Build a prefix of the header data by concatenating the strings
#   h<hexnum>v<hexnum> in header sorted order, where the hexnum are
#   the length of the header name and its value in lowercase hex,
#   respectively. Append one "#" character, followed by the header
#   names and values, again in header sorted order.
#
#   Compute SHA1 HMAC of this string with the secret key. Convert the
#   HMAC to a hex string, two lowercase hex characters per byte, 40
#   characters in total. If the resulting string compares byte for
#   byte equal with the CMS-AuthN-HMAC header value, the application
#   can trust the authentication and authorisation header values.
#   Since string consists of hexadecimal letters, it's always ASCII.
#
#  CMS-Auth-Host
#  CMS-Auth-Cert
#
#   These are legacy headers and should not be used in new apps.
#
# The module may also request the client to set a "cms-auth" cookie.
# For legacy reasons the cookie is set on X509 certificate accesses.
#
# Configuration parameters:
#  AUTH_HMAC_KEYS     Directory containing secret keys for HMAC signatures.
#  AUTH_HOST_EXEMPT   List of files with exempted host ip-address name pairs.
#  AUTH_GRID_MAPS     List of files with additional cert VO memberships.
#  AUTH_REVOKED       List of files containing revoked users.
#  AUTH_JSON_MAP      File containing SiteDB authn/authz info from mkauthmap.

package cmsauth;
use strict;
use warnings;
use Encode ();
use Apache2::ServerUtil;
use Apache2::Const -compile => ':common', ':http';
use Digest::HMAC_SHA1 'hmac_sha1';
use File::Spec::Functions 'rel2abs';
use File::Temp ':mktemp';
use HTML::Entities;
use Compress::Zlib;
use MIME::Base64;
use Sys::Hostname;
use JSON::XS 'decode_json';
use cmstools;
use CGI;

sub request_server_name($);
sub authn_fail($$);
sub init($);
sub authz_maybe_reload($);
sub authn_step($$);
sub authz_complete($$$%);
sub authn_host($$);
sub authn_cert($$);
sub authn_aucookie($$);
sub make_auth_cookie($$$$);
sub parse_auth_cookie($);
sub decode_auth_cookie($);

my $authz_json_file;
my $authz_json_stat = " ";
my %authz_by_dn;
my %authz_by_login;
my $NULL_COOKIE = ";path=/;secure;httponly;expires=Thu, 01-Jan-1970 00:00:01 GMT";
my $initialised = 0;
my %host_exempt = ();
my $server_name;
my %vocms;
my %revoked = (HOST => {}, LOGIN => {}, DN => {});

my $troubledoc = <<'END_OF_DOC';
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
 <head>
 <title>CMSWEB authentication help</title>
 <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
 <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
 <link rel="stylesheet" type="text/css" media="screen" href="/css/cmsweb.css" />
</head>
<body>
 <div id="main">
  <div id="top">
   <div class="boxTitle"><img src="/img/title.gif" alt="CMSWEB (title)" /></div>
  </div>
  <div id="middle">
   <div class="boxLinkContainer">
    <h2>Certificate authentication help</h2>
    {MESSAGE}
   </div>
  </div>
  <div id="bottom">
   <div class="boxFooter">&nbsp;</div>
  </div>
 </div>
</body>
</html>
END_OF_DOC

# Handler for logging out: removes any client cookies.
sub auth_logout_handler : method
{
  my ($class, $r) = @_;

  # Initialise on first request.
  init($r) if ! $initialised;

  # Get client-visible server name.
  my $server = request_server_name($r);

  # Redirect to server root but nuke cookies as we go.
  $r->headers_out->set("Location" => $server);
  $r->err_headers_out->add("Set-Cookie" => "cms-preauth=$NULL_COOKIE");
  $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
  return Apache2::Const::REDIRECT;
}

# Handler to present a web page to assist cert auth diagnosis.
sub auth_trouble_handler : method
{
  my ($class, $r) = @_;
  $me = "[cookie-auth/$$]" if ! $me;

  # Only permit access in HTTPS mode.  This ought to be caught
  # earlier on in server configuration, make last resort check here.
  return Apache2::Const::FORBIDDEN if ! $r->connection->is_https();

  # Initialise on first request.
  init($r) if ! $initialised;

  # Reload authorisation information if necessary.
  authz_maybe_reload($r);

  # Get current server name.
  my $server = request_server_name($r);

  # Check the client address has not been revoked access to this server.
  my $remote_addr = $r->connection->remote_addr->ip_get;
  return Apache2::Const::FORBIDDEN if exists $revoked{HOST}{$remote_addr};

  # Refuse to talk if the client is faking any headers.
  return Apache2::Const::FORBIDDEN if grep /^cms-(auth|client)/io, keys %{$r->headers_in};

  # If there is 'Origin' header, verify it is right.
  my $origin = $r->headers_in->get("Origin");
  return Apache2::Const::FORBIDDEN if $origin and $origin ne $server;

  # Build result based on authentication data.
  my $ir = initialreq($r);
  my $browser = $r->headers_in->get('User-Agent') || '';
  my $message = "";

  # Extract certificate data from the original HTTP request.
  my $verify = $ir->subprocess_env->get('SSL_CLIENT_VERIFY');
  my $cert_data = $ir->subprocess_env->get('SSL_CLIENT_CERT');
  my $dn = $ir->subprocess_env->get('SSL_CLIENT_S_DN');
  my $vremain = $ir->subprocess_env->get('SSL_CLIENT_V_REMAIN');
  my $vstart = $ir->subprocess_env->get('SSL_CLIENT_V_START');
  my $vend = $ir->subprocess_env->get('SSL_CLIENT_V_END');
  my $iscms;

  # For now we pretend strings are UTF-8, so we force the UTF-8 flag
  # on. This is actually the case only with Apache 2.3+, in earlier
  # versions it's the raw ASN.1 byte stream, usually subsets of ASCII.
  Encode::_utf8_on($dn);

  # Analyse the DN.
  if (! $dn)
  {
    # FIXME: Browser-specific advice?
    $message .= "<p>Your browser did not offer any certificate."
              . " Check that you have installed a grid certificate "
	      . " by suitable certificate authority and your browser "
	      . " trust settings offer that certificate to this site.</p>";
  }
  elsif (! utf8::is_utf8($dn))
  {
    $dn = encode_entities($dn);
    $message .= "<p>Your browser offered a DN '$dn' which was rejected"
              . " because it is not UTF-8.</p>";
  }
  elsif ($dn =~ /[\x00-\x1f]/)
  {
    $dn = encode_entities($dn);
    $message .= "<p>Your browser offered a DN '$dn' which was rejected"
              . " because of unsafe characters in range 0x00 - 0x1f.</p>";
  }
  elsif ($dn !~ m{^/(?:C|O|DC)=.*/CN=.})
  {
    $dn = encode_entities($dn);
    $message .= "<p>Your browser offered a DN '$dn' which was rejected"
              . " because it doesn't match structure of acceptable"
	      . " certificates. It doesn't start with C, O or DC"
	      . " field or is missing CN field.</p>";
  }
  else
  {
    $dn = encode_entities($dn);
    $message .= "<p>Your browser offered valid DN '$dn'.</p>";
  }

  my $expired = ! ($vremain > 0);
  $vstart = "(None)" if ! defined $vstart;
  $vend = "(None)" if ! defined $vend;
  $vremain = "(None)" if ! defined $vremain;
  $message .= "<p>Your certificate "
  	    . ($expired ? "has expired; it was valid" : "is valid")
	    . " from $vstart to $vend; $vremain days of validity remain.</p>";

  # Report any other failure.
  if ($verify ne 'SUCCESS')
  {
    $message .= "<p>You certificate failed basic validation, the"
    	        . " error was: " . encode_entities($verify) . ".</p>";
  }
  else
  {
    $message .= "<p>Your certificated passed basic validation.</p>";
  }

  # Check if the DN has been revoked access to this server.
  if ($dn && exists $revoked{DN}{$dn})
  {
    $message .= "<p>Access administratively disabled.</p>";
  }

  # Certificate is valid. Check it belongs to our VO.
  if ($dn && exists $vocms{$dn})
  {
    $message .= "<p>Your certificate is a CMS VO member.</p>";
  }
  elsif ($dn && ($dn =~ m{(.*?)(?:(?:/CN=\d+|/CN=proxy)|(/CN=limited proxy))+$}o
                 && exists $vocms{$1}))
  {
    $message .= "<p>Your certificate is a " . ($2 ? "limited ": "")
                . "proxy of a CMS VO member.</p>";
  }
  else
  {
    $message .= "<p>Your certificate is not registered member of the"
              . " CMS VO. You need to register at <a href='"
              . "https://voms2.cern.ch:8443/voms/cms"
	      . "'>VOMS</a> after which it will take up to six hours"
              . " for us to get the information.</p>"
  }

  if ($dn && exists $authz_by_dn{$dn})
  {
    $message .= "<p>Your certificate is mapped to the username '"
             . $authz_by_dn{$dn}{LOGIN} . "' in SiteDB.</p>";
  }
  elsif ($dn && ($dn =~ m{(.*?)(?:(?:/CN=\d+|/CN=proxy)|(/CN=limited proxy))+$}o
                 && exists $authz_by_dn{$1}))
  {
    $message .= "<p>Your certificate is mapped to the username '"
             . $authz_by_dn{$1}{LOGIN} . "' in SiteDB.</p>";
  }
  else
  {
    $message .= "<p>Your certificate is not mapped to any user"
              . " in SiteDB. Go to the CERN certificate mapping"
              . " <a href='https://resources.web.cern.ch/resources/Manage/Accounts/MapCertificate.aspx'>"
              . "page</a>, remove all existing mappings and add your certificate."
              . " The information should take up to one hour to propagate.</p>"
  }

  $message .= "<p>For more details please see <a href='"
   . "https://twiki.cern.ch/twiki/bin/view/CMS/DQMGUIGridCertificate'>"
   . "certificate setup instructions</a> for the most commonly needed"
   . " steps.</p>";

  my $body = $troubledoc;
  $body =~ s/\{MESSAGE\}/$message/g;
  $r->content_type('text/html');
  $r->print($body);
  return Apache2::Const::OK;
}

# Master HTTP request handling routine authentication check on a path.
sub auth_verify_handler : method
{
  my ($class, $r) = @_;
  $me = "[cookie-auth/$$]" if ! $me;

  # Only permit authentication in HTTPS mode.  This ought to be caught
  # earlier on in server configuration, make last resort check here.
  return authn_fail($r, "authentication denied without https")
    if ! $r->connection->is_https();

  # Initialise on first request.
  init($r) if ! $initialised;

  # Reload authorisation information if necessary.
  authz_maybe_reload($r);

  # Get current server name.
  my $server = request_server_name($r);

  # Check the client address has not been revoked access to this server.
  my $remote_addr = $r->connection->remote_addr->ip_get;
  return authn_fail($r, "authorisation revoked for host $remote_addr")
    if exists $revoked{HOST}{$remote_addr};

  # If there is 'Origin' header, verify it is right.
  my $origin = $r->headers_in->get("Origin");
  return Apache2::Const::FORBIDDEN if $origin and $origin ne $server;

  # Make sure authentication-related headers and environment are unset.
  # This prevents incoming request from faking any headers. Later we
  # only set headers relevant to this specific request.
  foreach (grep /^cms-(auth|client)/io, keys %{$r->headers_in})
  {
    $r->log->warn("$me clearing incoming authn/authz header $_");
    $r->headers_in->unset($_);
  }

  # Get the AUTH_SPEC steps from the original request. Allow this to
  # happen only during internal rewriting. Then process the request.
  my $ir = initialreq($r);
  return authn_fail($r, "authentication must be an internal redirection")
    if ! defined $ir->subprocess_env('AUTH_SPEC');

  return authn_step($r, { NEXT => [split /;/, $ir->subprocess_env('AUTH_SPEC')] });
}

# Return URL prefix for this request. Defaults to using "Host" request
# header prefixed with the scheme (http:// or https://), otherwise
# $server_name global variable. Note that if the client lies about
# the "Host" header, it can cause the server to redirect elsewhere.
sub request_server_name($)
{
  my ($r) = @_;
  my $host = $r->headers_in->get("Host");
  my $scheme = "http" . ($r->connection->is_https() ? "s" : "") . "://";
  my $name = $host ? ($scheme . $host) : $server_name;
  return $name;
}

# Internal utility function to fail the request.
sub authn_fail($$)
{
  my ($r, $reason) = @_;
  my $ir = initialreq($r);
  $r->log->warn("$me $reason; forbidding @{[$ir->unparsed_uri]}");
  $r->uri($ir->unparsed_uri);
  $r->status(Apache2::Const::FORBIDDEN);
  return Apache2::Const::FORBIDDEN;
}

# Per-server initialisation.  Set up cookie verification keys and list
# of hosts exempted from authentication.
sub init($)
{
  my $r = shift;
  my $server = $r->server;
  my $server_root = Apache2::ServerUtil::server_root();
  $server_name = "https://" . $server->server_hostname
                 . ($server->port != 443 ? ":" . $server->port : "");

  # Open /dev/urandom for aucookie.
  open(RND, "/dev/urandom") or die;

  # Read in cookie keys from AUTH_HMAC_KEYS directories.
  # Make sure we have keys to work with.
  if (! secret_load(map { rel2abs($_, $server_root) }
		    $r->dir_config->get("AUTH_HMAC_KEYS"))
      || ! secret_key("auth-sid")
      || ! secret_key("auth-csrf")
      || ! secret_key("auth-hn")
      || ! secret_key("auth-pass")
      || ! secret_key("cert-cookie")
      || ! secret_key("authz-headers"))
  {
    $r->log->error("$me no hmac keys, please create at least"
	           . " one key with update-keys, then"
		   . " restart with AUTH_HMAC_KEYS correctly set");
    die;
  }

  # Read in host exemption lists.
  foreach my $f ($r->dir_config->get("AUTH_HOST_EXEMPT"))
  {
    $f = rel2abs($f, $server_root);
    if (! open(F, "< $f"))
    {
      $r->log->error("$me AUTH_HOST_EXEMPT $f: $!");
      die;
    }

    while (<F>)
    {
      chomp; s/\#.*//; s/^\s+//; s/\s+$//;
      next if /^$/;
      my @items = split(/\s+/);
      if (scalar @items != 2)
      {
        $r->log->error("$me $f:$.: line not understood");
        die;
      }
      $host_exempt{$items[0]} = $items[1];
    }
    close(F);
  }

  # Read VO member definitions.
  foreach my $f ($r->dir_config->get("AUTH_GRID_MAPS"))
  {
    $f = rel2abs($f, $server_root);
    if (! open(F, "< $f"))
    {
      $r->log->error("$me AUTH_GRID_MAPS $f: $!");
      die;
    }

    while (<F>)
    {
      chomp; s/^\s+//; s/\s+$//;
      if (/"(.*)" ([a-z]+)$/)
      {
        $vocms{$1} = 1 if $2 eq 'cms';
      }
      elsif (! /^$/)
      {
        $r->log->error("$me $f:$.: line not understood");
        die;
      }
    }

    close(F);
  }

  if (! scalar %vocms)
  {
    $r->log->error("$me no CMS VO members found in AUTH_GRID_MAPS");
    die;
  }

  # Read in revoked users.
  foreach my $f ($r->dir_config->get("AUTH_REVOKED"))
  {
    $f = rel2abs($f, $server_root);
    if (! open(F, "< $f"))
    {
      $r->log->error("$me AUTH_REVOKED $f: $!");
      die;
    }

    while (<F>)
    {
      chomp; s/^\s+//; s/\s+$//; s/^#.*//;
      if (/^(dn|login|host):\s+(.*)$/)
      {
        $revoked{uc $1}{$2} = 1;
      }
      elsif (! /^$/)
      {
        $r->log->error("$me $f:$.: line not understood");
        die;
      }
    }

    close(F);
  }

  # Remember authn/authz json file if any.
  $authz_json_file = $r->dir_config->get("AUTH_JSON_MAP");

  $initialised = 1;
}

# Reload SiteDB authentication and authorisation information. The data
# is updated periodically by a separate process. The update is atomic,
# and the file is modified only if the data has actually changed. Load
# the new data on any request after the JSON file has changed, so all
# HTTPD processes tend to see the same data after the file changes.
sub authz_maybe_reload($)
{
  # If we don't have a file, do not change any state. While mkauthmap
  # should update the file atomically in place, don't let ops flukes
  # disable authn/z in the front-end.
  return if ! $authz_json_file;

  # If the file hasn't change since last we looked, no update needed.
  my $stat = join(" ", map { $_ || "" } -M $authz_json_file, -s _);
  return if $stat eq $authz_json_stat;

  # Reload the JSON data.
  open(JSON, "<", $authz_json_file) || return;
  my $data = do { local $/ = undef; scalar <JSON> };
  close(JSON);

  # Rebuild authz tables.
  %authz_by_dn = ();
  %authz_by_login = ();
  my $people = decode_json($data);
  foreach my $p (@$people)
  {
    $authz_by_login{$$p{LOGIN}} = $p if $$p{LOGIN} && ! $authz_by_login{$$p{LOGIN}};
    $authz_by_dn{$$p{DN}} = $p if $$p{DN} && ! $authz_by_dn{$$p{DN}};
  }

  # Remember last update time.
  $authz_json_stat = $stat;
}

# Internal utility to go to the next stage of authentication.
sub authn_step($$)
{
  my ($r, $opts) = @_;

  # If no more authentication steps left, and authentication is optional,
  # pass the request through with cleared authentication headers.  Fail
  # the request entirely otherwise.
  if (! @{$$opts{NEXT}})
  {
    if ($$opts{OPTIONAL})
    {
      $r->subprocess_env->set("AUTH_DONE" => "OK");
      $r->headers_in->set("CMS-Auth-Status" => "NONE");
      return authz_complete(initialreq($r), $r, $opts, METHOD => "None");
    }
    else
    {
      return authn_fail($r, "all authentication method failed");
    }
  }

  # Try next authentication method.
  my $method = shift(@{$$opts{NEXT}});
  if ($method eq 'optional')
  {
    $$opts{OPTIONAL} = 1;
    return authn_step($r, $opts);
  }
  elsif ($method eq 'authz=off')
  {
    $$opts{AUTHZ_NONE} = 1;
    return authn_step($r, $opts);
  }
  elsif ($method eq 'groups=(.*)')
  {
    push(@{$$opts{AUTHZ_GROUPS}}, qr/^$1$/o);
    return authn_step($r, $opts);
  }
  elsif ($method eq 'roles=(.*)')
  {
    push(@{$$opts{AUTHZ_ROLES}}, qr/^$1$/o);
    return authn_step($r, $opts);
  }
  elsif ($method eq 'host')
  {
    return authn_host($r, $opts);
  }
  elsif ($method eq 'cert')
  {
    return authn_cert($r, $opts);
  }
  elsif ($method eq 'limited-proxy')
  {
    $$opts{ALLOW_LIMITED_PROXY} = 1;
    return authn_step($r, $opts);
  }
  elsif ($method eq 'aucookie')
  {
    return authn_aucookie($r, $opts);
  }
  else
  {
    return authn_fail($r, "authentication method $$method not recognised");
  }
}

# Add authorisation information to the request headers for backends.
sub authz_complete($$$%)
{
  my ($ir, $r, $opts, %args) = @_;
  if (! $$opts{AUTHZ_NONE})
  {
    my %hdrs = ("cms-authn-method" => $args{METHOD});
    my $uinfo;

    if (! $uinfo && $args{DN})
    {
      my $utf8dn = $args{DN};
      utf8::encode($utf8dn);
      $hdrs{"cms-authn-dn"} = $utf8dn;
      $uinfo = $authz_by_dn{$args{DN}}
        if exists $authz_by_dn{$args{DN}};
    }

    if (! $uinfo && $args{LOGIN})
    {
      $hdrs{"cms-authn-login"} = $args{LOGIN};
      $uinfo = $authz_by_login{$args{LOGIN}}
        if exists $authz_by_login{$args{LOGIN}};
    }

    if ($uinfo)
    {
      my ($r, @g, %groups, @roles);
      foreach $r (rxfilter($$opts{AUTHZ_ROLES}, sort keys %{$$uinfo{ROLES}}))
      {
        if (@g = rxfilter($$opts{AUTHZ_GROUPS}, @{$$uinfo{ROLES}{$r}}))
        {
	  push(@{$groups{$r}}, @g);
          push(@roles, $r);
        }
      }

      my $utf8dn = $$uinfo{DN};
      my $utf8name = $$uinfo{NAME};
      utf8::encode($utf8dn) if $utf8dn;
      utf8::encode($utf8name) if $utf8name;
      $hdrs{"cms-authn-dn"} = $utf8dn if $utf8dn;
      $hdrs{"cms-authn-login"} = $$uinfo{LOGIN};
      $hdrs{"cms-authn-name"} = $utf8name if $utf8name;
      $hdrs{"cms-authz-$_"} = "@{$groups{$_}}" for @roles;
    }

    my @h = sort { $a cmp $b } keys %hdrs;
    my $auth = sprintf(("h%xv%x" x scalar @h) . "#" . ("%s" x (2 * scalar @h)),
		       (map { (length($_), length($hdrs{$_})) } @h),
		       (map { ($_, $hdrs{$_}) } @h));
    $hdrs{"cms-authn-hmac"} = secret_hmac("authz-headers", $auth);
    $r->headers_in->set($_ => $hdrs{$_}) for keys %hdrs;
  }

  $r->internal_redirect("/auth/complete" . $ir->unparsed_uri);
  return Apache2::Const::OK;
}

# Authentication routine for host-based authentication.
sub authn_host($$)
{
  my ($r, $opts) = @_;

  # Check if the remote host is in the exemption map.
  my $remote_addr = $r->connection->remote_addr->ip_get;
  my $host = $host_exempt{$remote_addr};

  # Pass to the next stage if not in the list of exempted hosts.
  return authn_step($r, $opts) if ! $host;

  # We accepted it. Add authentication headers to the request.
  $r->subprocess_env->set("AUTH_DONE" => "OK");
  $r->headers_in->set("CMS-Auth-Status" => "OK");
  $r->headers_in->set("CMS-Auth-Host" => "$remote_addr $host");
  return authz_complete(initialreq($r), $r, $opts, METHOD => "HostIP");
}

# Authentication routine for client certificate. The server's SSL path
# always attempts SSL client verification. Hence we have all the info
# needed always here, and there is no need to use cookies.
sub authn_cert($$)
{
  my ($r, $opts) = @_;
  my $ir = initialreq($r);

  # Extract certificate data from the original HTTP request.
  my $verify = $ir->subprocess_env->get('SSL_CLIENT_VERIFY');
  my $cert_data = $ir->subprocess_env->get('SSL_CLIENT_CERT');
  my $dn = $ir->subprocess_env->get('SSL_CLIENT_S_DN');
  my $vremain = $ir->subprocess_env->get('SSL_CLIENT_V_REMAIN');
  my $vstart = $ir->subprocess_env->get('SSL_CLIENT_V_START');
  my $vend = $ir->subprocess_env->get('SSL_CLIENT_V_END');
  my $iscms;

  # The following is merely to produce better error reports on cert
  # validation, with no change of result. First report gross errors.
  # However silently keep plodding if there is no DN at all.
  return authn_step($r, $opts) if ! $dn;

  # For now we pretend strings are UTF-8, so we force the UTF-8 flag
  # on. This is actually the case only with Apache 2.3+, in earlier
  # versions it's the raw ASN.1 byte stream, usually subsets of ASCII.
  Encode::_utf8_on($dn);

  # Report failure if DN seems funny.
  if (! utf8::is_utf8($dn)
      || $dn =~ /[\x00-\x1f]/
      || $dn !~ m{^/(?:C|O|DC)=.*/CN=.})
  {
    $r->log->notice("$me rejecting unexpected certificate $dn,"
	            . " verify $verify, vstart $vstart, vend $vend,"
		    . " vremain $vremain");
    return authn_step($r, $opts);
  }

  # Report failure if the certificate has expired.
  if (! ($vremain > 0))
  {
    $r->log->notice("$me rejecting expired certificate $dn,"
	            . " verify $verify, vstart $vstart, vend $vend,"
		    . " vremain $vremain");
    return authn_step($r, $opts);
  }

  # Report any other failure.
  if ($verify ne 'SUCCESS')
  {
    $r->log->notice("$me rejecting invalid certificate $dn,"
	            . " verify $verify, vstart $vstart, vend $vend,"
		    . " vremain $vremain");
    return authn_step($r, $opts);
  }

  # Check if the DN has been revoked access to this server.
  return authn_fail($r, "authorisation revoked for dn $dn")
    if exists $revoked{DN}{$dn};

  # Certificate is valid. Now make it unicode.
  utf8::decode($dn);

  # Check the certificate belongs to our VO.
  my $method;
  if (exists $vocms{$dn})
  {
    $method = "X509Cert";
  }
  elsif ($dn =~ m{(.*?)(?:/CN=\d+|/CN=proxy)+$}o && exists $vocms{$1})
  {
    $dn = $1;
    $method = "X509Proxy";
  }
  elsif ($$opts{ALLOW_LIMITED_PROXY}
         && $dn =~ m{(.*?)(?:/CN=\d+|/CN=proxy|/CN=limited proxy)+$}o
         && exists $vocms{$1})
  {
    $dn = $1;
    $method = "X509LimitedProxy";
  }
  else
  {
    $r->log->notice("$me rejecting non-vo certificate $dn,"
	            . " verify $verify, vstart $vstart, vend $vend,"
		    . " vremain $vremain");
    return authn_step($r, $opts);
  }

  # For backward compatibility generate a bogus cookie. Some clients
  # want one, and more importantly expect to be able to come back over
  # SSL _without_ certificate, offering the cookie. Generate a random
  # 20-byte token signed with our secret key, printed out in hex. We
  # can later verify in 'aucookie' we gave that token out so client is
  # legit. The token is valid as long until our secret key is rotated
  # (every few hours). In practice a few seconds will suffice. Note
  # that this cookie will be set as expired one, so only 'stupid'
  # clients that don't parse the cookie will honour it.
  #
  # NB: This is just for backwards compatibility.
  if (grep(/(?:Prod|WM)Agent|visDQMUpload|[Pp]ython|curl/o,
	   $r->headers_in->get('User-agent')))
  {
    my $keydata;
    if (sysread(RND, $keydata, 20) != 20)
    {
      $r->log->error("error while generating aucookie token: $!");
      return authn_step($r, $opts);
    }

    my $cookiedata = unpack("h*", $keydata) . secret_hmac("cert-cookie", $keydata);
    my $cookie = sprintf("cms-auth=%s;path=/;secure;httponly;"
		         ."expires=Thu, 01-Jan-1970 00:00:01 GMT",
		         $cookiedata);

    my $cookies = join("; ", $r->headers_in->get("Cookie"));
    $r->err_headers_out->add("Set-Cookie" => $cookie);
    $r->headers_in->set("Cookie" => join("; ", grep($_, $cookiedata, $cookies)));
  }

  # We accepted it. Add authentication headers to the request.
  my $utf8dn = $dn;
  utf8::encode($utf8dn);
  $r->subprocess_env->set("AUTH_DONE" => "OK");
  $r->headers_in->set("CMS-Auth-Status" => "OK");
  $r->headers_in->set("CMS-Auth-Cert" => $utf8dn);
  return authz_complete($ir, $r, $opts, METHOD => $method, DN => $dn);
}

# Authentication routine for backwards compatible client certificate with
# a cookie. This remains required until Tier-0 expects to make X509 cert
# request, which generates a cookie which the client then can use to make
# another HTTP request _without_ X509 info. This is a minimal routine
# without any authorisation. The authn_cert() routine sets a cookie we
# can verify here.
sub authn_aucookie($$)
{
  my ($r, $opts) = @_;
  my $ir = initialreq($r);

  # Check if we have a backwards compatible authn cookie: 80 lowercase
  # hex characters. The first 20*2 are random junk, the other 20*2 is
  # SHA1 hash of the junk with our secret key.
  my $cookie = cookie_from_header($r, 'cms-auth');
  return authn_step($r, $opts)
    if (! $cookie
        || $cookie !~ /^([0-9a-f]{40})([0-9a-f]{40})$/
	|| ! secret_hmac_check("cert-cookie", pack("h*", $1), $2));

  # The junk matched are server key, pass through.
  $r->subprocess_env->set("AUTH_DONE" => "OK");
  $r->headers_in->set("CMS-Auth-Status" => "OK");
  return authz_complete($ir, $r, $opts, METHOD => "AUCookie");
}

# Create authentication cookie for Set-Cookie header. The arguments
# are cookie type, validity time, and two lists for keys and values.
# The payload keys and values are
# added encoded to the cookie in base64-encoded compressed form.
# A SHA1 HMAC is appeneded to the cookie to prevent tampering.
sub make_auth_cookie($$$$)
{
  my ($type, $until, $keys, $vals) = @_;
  $until = sprintf("%x", time() + $until);

  my $data = sprintf(join("", map { "$_%x" } @$keys), map { length $_ } @$vals);
  $data = base64(compress($data . "#" . join("", @$vals)));

  my $hmaclen= 28; # SHA-1 hash = 160 bits = 20 bytes = 28 base64
  my ($secret, $key) = secret("auth-hn");
  my $cookie = sprintf("t%xu%xs%xp%xh%x#",
	               length $type, length $until,
	  	       length $secret, length $data,
		       $hmaclen);
  $cookie .= join("", $type, $until, $secret, $data);
  $cookie .= base64(hmac_sha1($cookie, $key));
  return "$cookie;path=/;secure;httponly";
}

# Decompose cookie from HTTP header into its constituents.  Verifies
# the cookie follows expected formatting, then retrieves the known
# parts of the format.  The cookie is formatted in several field with
# explicitly encoded meaning, length, and payload data.  This format
# prevents tampering with the fields, including fooling this routine
# to mis-interpret the data in the cookie.
sub parse_auth_cookie($)
{
  my $cookie = shift;
  my $hex = "[0-9a-f]+";
  if ($cookie && $cookie =~ /^t($hex)u($hex)s($hex)p($hex)h($hex)#(.*)$/)
  {
    my $typelen = hex($1);
    my $explen = hex($2);
    my $keylen = hex($3);
    my $datalen = hex($4);
    my $hashlen = hex($5);
    my $rest = $6;

    if (length($rest) == $typelen + $explen + $keylen + $datalen + $hashlen
	&& $typelen == 1
	&& $explen == 8
    	&& $keylen == 5
	&& $datalen < 3000
	&& $hashlen == 28)
    {
      my $pos    = 0;
      my $type   = substr($rest, $pos, 1); $pos += 1;
      my $until  = substr($rest, $pos, $explen); $pos += $explen;
      my $secret = substr($rest, $pos, $keylen); $pos += $keylen;
      my $data   = substr($rest, $pos, $datalen); $pos += $datalen;
      my $hmac   = substr($rest, $pos, $hashlen); $pos += $hashlen;

      if ($secret =~ /^[A-Z\d]+$/ && $until =~ /^$hex$/)
      {
        return { TYPE => $type, SECRET => $secret, UNTIL => hex($until),
		 DATA => $data, HMAC => $hmac, TEXT => $cookie,
	 	 VFYTEXT => substr($cookie, 0, -28) };
      }
    }
  }

  return undef;
}

# Decode payload data from a cookie value created make_auth_cookie().
sub decode_auth_cookie($)
{
  my $hex = "[0-9a-f]+";
  my $val = do { no warnings; uncompress(decode_base64(shift)); };
  return undef if ! defined $val or $val !~ /^([A-Za-z0-9]+)#(.*)/;

  my $data = {};
  my $keys = $1;
  my $vals = $2;
  my $pos = 0;
  while ($keys =~ /\G([A-Za-z])($hex)/g)
  {
    my $len = hex($2);
    $$data{$1} = substr($vals, $pos, $len);
    $pos += $len;
  }

  return $data;
}

1;
