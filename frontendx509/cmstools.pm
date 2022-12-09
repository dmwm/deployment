package cmstools;
use strict;
use warnings;
use base 'Exporter';
use Apache2::ServerUtil;
use Digest::HMAC_SHA1 'hmac_sha1_hex';
use MIME::Base64;

our @EXPORT = qw(cookie_from_header rxfilter initialreq
                 dbsql dbprep dbbindexec dbexec base64
		 secret secret_name secret_key secret_exists
		 secret_hmac secret_hmac_check secret_load
                 $me $log_all_sql);

my $me;
my $log_all_sql = 0;
my %secrets;

sub secret($;$);
sub secret_name($;$);
sub secret_key($;$);
sub secret_exists($$);
sub secret_hmac($$);
sub secret_hmac_check($$$);
sub secret_load(@);

sub base64($);
sub cookie_from_header($$);
sub rxfilter($@);
sub initialreq($);
sub dbsql($;$);
sub dbprep($$);
sub dbbindexec($%);
sub dbexec($$%);

# Pick current secret. Returns pair of the name of the secret
# and the actual HMAC key value.
sub secret($;$)
{
  my ($kind, $name) = @_;
  die "secret of type $kind does not exist"
    if ! exists $secrets{$kind};

  if (ref $secrets{$kind})
  {
    die "secret of type $kind has no keys"
      if ! keys %{$secrets{$kind}};
    $name = (sort { $b cmp $a } keys %{$secrets{$kind}})[0]
      if (! defined $name || !  exists $secrets{$kind}{$name});
    return ($name, $secrets{$kind}{$name});
  }
  else
  {
    return (undef, $secrets{$kind});
  }
}

# Return the name of the current secret.
sub secret_name($;$)
{
  my ($kind, $name) = @_;
  return (secret($kind, $name))[0];
}

# Return the HMAC key of the current secret.
sub secret_key($;$)
{
  my ($kind, $name) = @_;
  return (secret($kind, $name))[1];
}

# Check if a secret is still known.
sub secret_exists($$)
{
  my ($kind, $name) = @_;
  return ref $secrets{$kind} && exists $secrets{$kind}{$name};
}

# Compute HMAC signature for some data given a secret key.
sub secret_hmac($$)
{
  my ($kind, $data) = @_;
  my $key = secret_key($kind);
  die if not defined $key;
  return hmac_sha1_hex($data, $key);
}

# Check if HMAC on data matches target HMAC with any known secret key.
sub secret_hmac_check($$$)
{
  my ($kind, $data, $target) = @_;
  die if not defined $secrets{$kind};
  if (ref $secrets{$kind})
  {
    foreach my $name (keys %{$secrets{$kind}})
    {
      my $key = $secrets{$kind}{$name};
      return 1 if hmac_sha1_hex($data, $key) eq $target;
    }
  }
  else
  {
    return 1 if hmac_sha1_hex($data, $secrets{$kind}) eq $target;
  }

  return 0;
}

# Read in cookie keys. We take list of directories, which may contain
# files or directories. If it's a file, it's a single secret key. If
# it's a directory, we read files in it and use them as alternate keys.
sub secret_load(@)
{
  my (@dirs) = @_;
  foreach my $f (map { @{[<$_/*>]} } @dirs)
  {
    local $/ = undef;
    my $key;
    my $fname = $f;
    $fname =~ s|.*/||;
    if (-d $f)
    {
      $secrets{$fname} ||= {};
      foreach $key (<$f/*>)
      {
	my $keyname = $key; $keyname =~ s|.*/||;
        next if exists $secrets{$fname}{$keyname};
	open(X, "< $key") or die "$key: $!\n";
	$secrets{$fname}{$keyname} = <X>;
	close(X);
      }
    }
    else
    {
      next if exists $secrets{$fname};
      open(X, "< $f") or die "$f: $!\n";
      $secrets{$fname} = <X>;
      close(X);
    }
  }

  return scalar keys %secrets;
}

# Shorthand for string-to-string base64 encoding.
sub base64($) { return encode_base64(shift, ''); }

# Retrieve a cookie from Apache HTTP request object.
#
# Retrieves one or more "Cookie" HTTP request headers from a request
# object. Each header consists of one or more cookie values separated
# by ';'. Each cookie value is of the form NAME[=VALUE], which may be
# followed by $ATTR[=VALUE] attributes.
#
# Returns the value of the first cookie with requested NAME with no
# '$Domain' attribute and no '$Path' or '$Path' equal to '/'. Returns
# an empty string if no such cookie is present in the given request.
sub cookie_from_header($$)
{
  my ($r, $name) = @_;
  my @toks = map { s/^\s+//; s/\s+$//; $_ }
             map { split /; ?/ }
	     $r->headers_in->get('Cookie');

  while (@toks)
  {
    my ($k, $v) = split("=", shift(@toks), 2);
    $v = '' if ! defined $v;

    my %attrs = ();
    while (@toks && substr($toks[0], 0, 1) eq '$')
    {
      my ($ak, $av) = split("=", shift(@toks), 2);
      $attrs{lc $ak} = $av;
    }

    return $v if ($k eq $name
	          && ! defined $attrs{'$domain'}
		  && (! defined $attrs{'$path'}
		      || $attrs{'$path'} eq "/"));
  }

  return '';
}

# Given a RXLIST and list of strings ARGS, return from ARGS strings
# which match any regular expression from RXLIST.  If RXLIST is
# undefined or an empty list, return ARGS unmodified.
sub rxfilter($@)
{
  my ($rxlist, @args) = @_;
  return @args if ! $rxlist || !@$rxlist;

  my @result;
  foreach my $arg (@args)
  {
    push(@result, $arg) if grep($arg =~ /$_/, @$rxlist);
  }
  return @result;
}

# Shorthand for getting initial request in internal redirects.
sub initialreq($)
{
  my $prev;
  my $r = shift;
  $r = $prev while ($prev = $r->prev);
  return $r;
}

# Rewrite a SQL statement. Insert optional schema prefix.
sub dbsql($;$)
{
  my ($sql, $pfx) = @_;
  $sql =~ s/--.*//mg;
  $sql =~ s/^\s+//mg;
  $sql =~ s/\s+$//mg;
  $sql =~ s/\n/ /g;
  $sql =~ s/(?<=\s)((t|seq|ix|pk|fk)_[A-Za-z0-9_]+)(?!\.)/$pfx.$1/g if $pfx;
  $sql =~ s/(?<=\s)((from|join)\s+)([A-Za-z0-9_]+)(?=$|\s)/$1$pfx.$3/g if $pfx;
  return $sql;
}

# Prepare a SQL statement. All statements are always cached
# so recursive use of a statement is not advised.
sub dbprep($$)
{
  my ($dbh, $sql) = @_;
  $sql = dbsql($sql, $$dbh{private_prefix});

  if (my $stmt = $$dbh{private_stmts}{$sql})
  {
    $stmt->finish();
    return $stmt;
  }

  return $$dbh{private_stmts}{$sql} = $dbh->prepare($sql);
}

# Bind and execute a SQL statement.
sub dbbindexec($%)
{
  my ($stmt, %params) = @_;
  if ($log_all_sql)
  {
    my $s = Apache2::ServerUtil->server;
    my $sql = $$stmt{Statement};
    $sql =~ s/\s+/ /g; $sql =~ s/^\s+//; $sql =~ s/\s+$//;
    my $bound = join (", ",
                      map { "($_, " . (defined $params{$_} ? $params{$_} : "undef") . ")" }
                      sort keys %params);
    $s->notice("$me executing sql '$sql' [$bound]");
  }

  my $isarray = 0;
  while (my ($param, $val) = each %params)
  {
    if (ref $val eq 'ARRAY')
    {
      $stmt->bind_param_array($param, $val);
      $isarray++;
    }
    elsif (ref $val)
    {
      $stmt->bind_param_inout($param, $val, 4096);
    }
    else
    {
      $stmt->bind_param($param, $val);
    }
  }

  # { ArrayTupleStatus => [] }
  return $isarray ? $stmt->execute_array() : $stmt->execute();
}

# Utility to prepare, bind and execute a SQL statement.
sub dbexec($$%)
{
  my ($dbh, $sql, %params) = @_;
  my $stmt = dbprep($dbh, $sql);
  my $rv = dbbindexec($stmt, %params);
  return wantarray ? ($stmt, $rv) : $stmt;
}

1;
