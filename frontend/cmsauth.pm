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
# CMS authorisation database (SiteDB). If the user is known and has
# authorisation roles, the information is added to the HTTP request
# headers. The back-end apps should use the information from headers
# to determine actions applicable to the user.
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
#  hnlogin
#
#   Allow access if the user has logged in using CMS hypernews login.
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
#     HNLogin    Client has logged in using CMS hypernews account.
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
#   is always present when CMS-AuthN-Method is X509Cert/Proxy, and if
#   CMS-AuthN-Method is HNLogin and SiteDB has DN account association.
#
#  CMS-AuthN-Login
#
#   The value of this header is the CMS hypernew login of the client.
#   It is always present always when CMS-AuthN-Method is HNLogin, and
#   if CMS-AuthN-Method is X509Cert/Proxy and SiteDB has DN account
#   association.
#
#  CMS-AuthN-Name
#
#   The value of this header is the SiteDB registered forename and
#   surname of the client. It may not be present if the fields have
#   not been recorded in SiteDB. If authentication method is HostIP
#   or None, this header is not present.
#
#  CMS-AuthZ-<Role>
#
#   A header for each role the client has, with space separated list
#   of group:name and site:name the role applies to. Note that all of
#   the entities -- roles, groups and sites -- are in canonical form
#   where the permitted letters are lowercase letters a-z, numbers
#   and the dash "-". All other characters are converted to "-" and
#   consecutive dashes are collapsed to one dash.
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
#
#  CMS-Auth-Host
#  CMS-Auth-Cert
#
#   These are legacy headers and should not be used in new apps.
#
# The module may also request the client to set a "cms-auth" cookie.
# For legacy reasons the cookie is set on X509 certificate accesses.
# In future the cookie will only be set on CMS hypernews logins.
#
# Configuration parameters:
#  AUTH_HMAC_KEYS     Directory containing secret keys for HMAC signatures.
#  AUTH_HOST_EXEMPT   List of files with exempted host ip-address name pairs.
#  AUTH_GRID_MAPS     List of files with additional cert VO memberships.
#  AUTH_REVOKED       List of files containing revoked users.
#  AUTH_DB_PARAMS     File containing SiteDB connection parameters.

package cmsauth;
use strict;
use warnings;
use Apache2::ServerUtil;
use Apache2::Const -compile => ':common', ':http';
use Digest::HMAC_SHA1 'hmac_sha1';
use File::Spec::Functions 'rel2abs';
use File::Temp ':mktemp';
use HTML::Entities;
use Compress::Zlib;
use MIME::Base64;
use Sys::Hostname;
use Apache::DBI;
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

my %authz_dbparam;
my @authz_dbargs;
my %authz_by_dn;
my %authz_by_login;
my %authz_warnings;
my $authz_reload = 0;
my $NULL_COOKIE = ";path=/;secure;httponly;expires=Thu, 01-Jan-1970 00:00:01 GMT";
my $initialised = 0;
my %host_exempt = ();
my $server_name;
my %vocms;
my %revoked = (HOST => {}, LOGIN => {}, DN => {});

my $hnlogindoc = <<'END_OF_DOC';
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
 <head>
 <title>CMSWEB HyperNews Login</title>
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
    <h2>Login with HyperNews account</h2>
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

# Handler for authentication via HyperNews account. Presents user a
# login form, including CSRF protection token and (for authentication
# only) session id cookie.
#
# Each time the form is generated it will have a fresh new session id
# and CSRF token, in part to prevent session fixation attacks. The
# authentication session id is the SSL session id of the SSL request,
# with HMAC to verify one of the servers in the cluster generated it.
# The CSRF token is a HMAC hash of (remote ip address, user agent,
# session-id). For each request we verify the session id and token;
# if they do not match the method simply acts as if no login occurred
# and presents the form again.
#
# The session id is stored as a cookie during the authentication, and
# removed afterwards. The CSRF token and service to transfer to are
# stored as hidden <input> parameters in the form.
#
# Note the code below relies on the fact that CGI's param() only
# returns POST body parameters; URL parameters are not returned.
sub auth_hnlogin_handler : method
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

  # Refuse to talk if the client fakes any sensitive headers.
  return Apache2::Const::FORBIDDEN if grep /^cms-(auth|client)/io, keys %{$r->headers_in};

  # If there is 'Origin' header, verify it is right.
  my $origin = $r->headers_in->get("Origin");
  return Apache2::Const::FORBIDDEN if $origin and $origin ne $server;

  # Check the form represents valid submission.
  my $form = new CGI;
  my $form_account = $form->param('a') || '';
  my $form_passwd = $form->param('p') || '';
  my $form_token = $form->param('t') || '';
  my $form_service = $form->param('c') || '/';
  my $url_service = $form->url_param('c') || '/';
  my $sid_token = cookie_from_header($r, "cms-preauth") || '';
  my $user_agent = $r->headers_in->get('User-Agent') || '';
  my @csrf = ($remote_addr, $user_agent, substr($sid_token, 0, 40));
  my $csrf_value = sprintf("r%xu%xs%x#%s%s%s", (map { length $_ } @csrf), @csrf);
  my $is_valid_submission
    = ($r->method() eq 'POST'
       && $form_service =~ m{^/([-a-z0-9_]+(/.*)?)?$}
       && $url_service =~ m{^/([-a-z0-9_]+(/.*)?)?$}
       && $form_account =~ m{^[a-z0-9]+(?:\.nocern|\.notcms)?$}
       && $form_passwd ne ''
       && $form_token =~ m{^[0-9a-f]{40}$}
       && $sid_token =~ /^([0-9a-f]{40})([0-9a-f]{40})$/
       && secret_hmac_check("auth-sid", $1, $2)
       && secret_hmac_check("auth-csrf", $csrf_value, $form_token));

  # If it's valid submission, check if it's also valid login.
  my $is_valid_login
    = ($is_valid_submission
       && exists $authz_by_login{$form_account}
       && defined $authz_by_login{$form_account}{PASSWD}
       && length $authz_by_login{$form_account}{PASSWD} >= 8
       && (crypt($form_passwd, substr($authz_by_login{$form_account}{PASSWD}, 0, 2))
	   eq $authz_by_login{$form_account}{PASSWD}));

  # If it's valid submission but invalid login, log it and force back.
  if ($is_valid_submission && ! $is_valid_login)
  {
    $r->log->error("$me login failed, user $form_account,"
	    	   . " sid $sid_token, csrf [@csrf]");
    $is_valid_submission = 0;
  }

  # If it wasn't a valid submission, generate the form afresh.
  # If this is an initial GET, then copy $url_service to form.
  if (! $is_valid_submission)
  {
    $form_service = $url_service if $r->method() eq 'GET';
    $form_service = encode_entities($form_service);

    my $ssl_sid = lc substr($r->subprocess_env->get("SSL_SESSION_ID"), 0, 40);
    return Apache2::Const::FORBIDDEN if length $ssl_sid < 40;

    my $sid = $ssl_sid . secret_hmac("auth-sid", $ssl_sid);
    my $cookie = $sid . ";path=/;secure;httponly";
    @csrf = ($remote_addr, $user_agent, $ssl_sid);
    $csrf_value = sprintf("r%xu%xs%x#%s%s%s", (map { length $_ } @csrf), @csrf);
    my $csrf_token = secret_hmac("auth-csrf", $csrf_value);

    my $message = "<form action='" . encode_entities($r->uri) . "' method='POST'>"
     . "<input type='hidden' name='t' value='$csrf_token' />"
     . "<input type='hidden' name='c' value='$form_service' />"
     . "<table cellspacing='3' cellpadding='5' border='0'>"
     . "<tr><td nowrap='nowrap' align='right'>Username:</td>"
     . "<td><input type='text' name='a' size='18' value='' /></td></tr>"
     . "<tr><td nowrap='nowrap' align='right'>Password:</td>"
     . "<td><input type='password' name='p' size='18' value='' /></td></tr>"
     . "<tr><td nowrap='nowrap' align='right'>&nbsp;</td>"
     . "<td><input type='submit' name='login' value='Sign In' /></td></tr>"
     . "</table></form>";

    my $body = $hnlogindoc;
    $body =~ s/\{MESSAGE\}/$message/g;
    $r->content_type('text/html');

    # Set session cookie. Clear any existing auth cookie.
    $r->err_headers_out->set("Set-Cookie" => "cms-preauth=$cookie");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");

    # Log-in form cannot be displayed in a frame.
    $r->headers_out->set("X-Frame-Options" => "DENY");

    # FIXME: Enable HTTP Strict Transport Security
    # $r->headers_out->set("Strict-Transport-Security" => "max-age=" . (365 * 86400));

    $r->print($body);
    return Apache2::Const::OK;
  }

  # It's a valid submission and login. Redirect to destination.
  # Install cookie to confirm authentication. The cookie depends
  # indirectly on the users's password, so user password change
  # invalidates all outstanding authentication tokens. The token
  # is tied to the browser user agent string, but not IP address.
  # We set cookie validity to one month, which makes its validity
  # actually defined by the update-keys secrets rotation schedule.
  my $uinfo = $authz_by_login{$form_account};
  $r->log->notice("$me accepted login for user $form_account,"
	          . " dn @{[$$uinfo{DN} || '']}, auth session $csrf[2],"
		  . " ua $user_agent");

  my $passkey = secret_hmac("auth-pass", "$form_account $$uinfo{PASSWD}");
  my $cookie = make_auth_cookie('L', 30 * 86400, [ qw(A D P S U) ],
	  		        [ $form_account, $$uinfo{DN} || '',
				  $passkey, $csrf[2], $user_agent ]);

  $r->headers_out->set("Location" => $server . $form_service);
  $r->err_headers_out->add("Set-Cookie" => "cms-preauth=$NULL_COOKIE");
  $r->err_headers_out->add("Set-Cookie" => "cms-auth=$cookie");
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

  # Analyse the DN.
  if (! $dn)
  {
    # FIXME: Browser-specific advice?
    $message .= "<p>Your browser did not offer any certificate."
              . " Check that you have installed a grid certificate "
	      . " by suitable certificate authority and your browser "
	      . " trust settings offer that certificate to this site.</p>";
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
  elsif ($dn
	 && (($dn =~ m{(.*?)/CN=\d+$}o && exists $vocms{$1})
	     || ($dn =~ m{(.*?)(?:/CN=proxy)+$}o && exists $vocms{$1})))
  {
    $message .= "<p>Your certificate is a proxy of a CMS VO member.</p>";
  }
  else
  {
    $message .= "<p>Your certificate is not registered member of the"
              . " CMS VO. You need to register at <a href='"
              . "https://lcg-voms.cern.ch:8443/vo/cms/vomrs?"
	      . "path=/RootNode&action=execute'>VOMS</a> after"
	      . " which it will take up to six hours for us to"
              . " get the information.</p>"
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

  # Connect to authz database if any.
  if (my $db = $r->dir_config->get("AUTH_DB_PARAMS"))
  {
    $db = rel2abs($db, $server_root);
    if (! open(F, "< $db"))
    {
      $r->log->error("$me $db: cannot read");
      die;
    }

    my $dbpfx = "";
    my $dbuser = "";
    my $dbpass = "";
    my $dbid = "cmsauth\@@{[Sys::Hostname::hostname()]}";
    my ($dbtype, $dbname);
    while (<F>)
    {
      chomp;
      s/#.*//;
      s/^\s+//;
      s/\s+$//;
      s/\s+/ /g;
      next if /^$/;
      if (/^type (\S+)$/) {
        $dbtype = $1;
      } elsif (/^database (\S+)$/) {
        $dbname = $1;
      } elsif (/^user (\S+)$/) {
        $dbuser = $1;
      } elsif (/^password (.*)$/) {
        $dbpass = $1;
      } elsif (/^id (\S+)$/) {
        $dbid = $1;
      } elsif (/^schema-prefix (\S+)$/) {
        $dbpfx = $1;
      } elsif (/^log-sql (\S+)$/) {
        $log_all_sql = 1 if ($1 eq 'yes' || $1 eq 'on');
      } else {
        $r->log->error("$me $db:$.: line not understood");
        die;
      }
    }
    close(F);

    if (! $dbtype || ! $dbname)
    {
      $r->log->error("$me $db: missing parameters");
      die;
    }

    @authz_dbargs = ("DBI:$dbtype:$dbname", $dbuser, $dbpass,
		     { RaiseError => 1, AutoCommit => 0,
		       PrintError => 0, ora_module_name => $dbid });
    %authz_dbparam = (FetchHashKeyName => "NAME_uc",
                      LongReadLen => 4096,
                      RowCacheSize => 10000,
                      private_prefix => $dbpfx);
  }

  $initialised = 1;
}

# Reload authentication and authorisation information from SiteDB,
# but only if at least one minute has passed from the previous use.
# As we have interest to make sure all HTTPD processes reload their
# roles about the same time to avoid inconsistent answers, we reload
# on first HTTP request after the UTC minute has rolled.
sub authz_maybe_reload($)
{
  return if ! @authz_dbargs;

  my $minute = int(time() / 60);
  return if $minute == $authz_reload;

  my ($req) = @_;
  $authz_reload = $minute;
  %authz_by_dn = ();
  %authz_by_login = ();
  my %uid;
  my $dbh;

  eval
  {
    $dbh = DBI->connect(@authz_dbargs);
    @$dbh{keys %authz_dbparam} = values %authz_dbparam;
    $$dbh{private_stmts} ||= {};

    # Read users and passwords.
    my $q = dbexec($dbh, qq{
      select c.id, c.username, c.forename, c.surname, c.dn, p.passwd
      from contact c left join user_passwd p on p.username = c.username});

    while (my $r = $q->fetchrow_arrayref())
    {
      my ($id, $login, $first, $last, $dn, $pass)
         = map { (defined $_ ? $_ : '') } @$r;
      $login = lc $login;
      # Fix up datatabase junk
      $login =~ s/^\s+//; $login =~ s/\s+$//;
      $dn =~ s/^\s+//; $dn =~ s/\s+$//;
      $dn =~ s/^DN unknown.*//;
      $dn =~ s/^\d+$//;

      # Skip any unsafe material
      if ("$dn:$login:$first:$last" =~ /[\x00-\x1f]/
          || ($dn ne '' && $dn !~ m{^/(?:C|O|DC)=.*/CN=.})
	  || $login !~ m{^[a-z0-9]*(?:\.nocern|\.notcms)?$})
      {
	if (! $authz_warnings{"login:$login"})
        {
          $r = [ map { (defined $_ ? $_ : '') } @$r ];
          $req->log->error("$me skipping unsafe user id $$r[0], login '$$r[1]',"
		           . " dn '$$r[4]', forename '$$r[2]', surname '$$r[3]'");
	  $authz_warnings{"login:$login"} = 1;
        }

	next;
      }

      # Build human name.
      my $name = join(" ", grep($_, $first, $last));

      # Remember this user.
      $authz_by_dn{$dn} = $authz_by_login{$login} = $uid{$id}
        = { ID => $id, LOGIN => $login, NAME => $name,
            DN => $dn, PASSWD => $pass, ROLES => {} };
    }

    # Read site and group roles of users.
    foreach my $sql (qq{select 'site' type, sr.contact, r.title, c.name
                        from site_responsibility sr
                        join role r on r.id = sr.role
                        join site s on s.id = sr.site
                        join site_cms_name_map sn on sn.site_id = s.id
                        join cms_name c on c.id = sn.cms_name_id},
		     qq{select 'group' type, gr.contact, r.title, g.name
                        from group_responsibility gr
                        join role r on r.id = gr.role
                        join user_group g on g.id = gr.user_group})
    {
      $q = dbexec($dbh, $sql);
      while (my $r = $q->fetchrow_arrayref())
      {
        my ($type, $id, $role, $name) = @$r;
        next if not exists $uid{$id};

        ($role = lc $role) =~ s/[^a-z0-9]+/-/g;
        ($name = lc $name) =~ s/[^a-z0-9]+/-/g;
        push(@{$uid{$id}{ROLES}{$role}}, "$type:$name");
      }
    }

    # Sort capabilities.
    foreach my $u (values %uid)
    {
      foreach my $r (values %{$$u{ROLES}})
      {
	splice(@$r, 0, scalar @$r, sort { $a cmp $b } @$r);
      }
    }
  };

  $req->log->error("$me database error: $@") if $@;
  eval { $dbh->rollback() } if $dbh;
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
  elsif ($method eq 'aucookie')
  {
    return authn_aucookie($r, $opts);
  }
  elsif ($method eq 'hnlogin')
  {
    return authn_hnlogin($r, $opts);
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
      $hdrs{"cms-authn-dn"} = $args{DN};
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

      $hdrs{"cms-authn-dn"} = $$uinfo{DN} if $$uinfo{DN};
      $hdrs{"cms-authn-login"} = $$uinfo{LOGIN};
      $hdrs{"cms-authn-name"} = $$uinfo{NAME} if $$uinfo{NAME};
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

  # Report failure if DN seems funny.
  if ($dn =~ /[\x00-\x1f]/ || $dn !~ m{^/(?:C|O|DC)=.*/CN=.})
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

  # Certificate is valid. Check it belongs to our VO.
  my $method;
  if (exists $vocms{$dn})
  {
    $method = "X509Cert";
  }
  elsif (($dn =~ m{(.*?)/CN=\d+$}o && exists $vocms{$1})
	 || ($dn =~ m{(.*?)(?:/CN=proxy)+$}o && exists $vocms{$1}))
  {
    $dn = $1;
    $method = "X509Proxy";
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
  $r->subprocess_env->set("AUTH_DONE" => "OK");
  $r->headers_in->set("CMS-Auth-Status" => "OK");
  $r->headers_in->set("CMS-Auth-Cert" => $dn);
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

# Authentication routine for hypernews account login.
sub authn_hnlogin($$)
{
  my ($r, $opts) = @_;
  my $ir = initialreq($r);

  # Check the user login cookie is valid.
  my $cookie_text = cookie_from_header($r, "cms-auth");
  return authn_step($r, $opts) if ! $cookie_text;

  # Check it's structurally valid.
  my $cookie = parse_auth_cookie($cookie_text);
  if (! $cookie)
  {
    $r->log->warn("$me rejecting cookie for parse error '$cookie_text'");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # Check the HMAC matches what we'd expect.
  my $s = secret_key("auth-hn", $$cookie{SECRET});
  my $hmac = base64(hmac_sha1($$cookie{VFYTEXT}, $s));
  if (! secret_exists("auth-hn", $$cookie{SECRET}))
  {
    $r->log->warn("$me rejecting cookie for invalid key '$$cookie{SECRET}'");
    return authn_step($r, $opts);
  }

  if ($hmac ne $$cookie{HMAC})
  {
    $r->log->warn("$me rejecting cookie for hmac mismatch '$$cookie{HMAC}'"
	          . " should be '$hmac'; cookie was '$cookie_text'");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # Check cookie type.
  if ($$cookie{TYPE} ne 'L')
  {
    $r->log->warn("$me rejecting cookie for unknown type '$$cookie{TYPE}'");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # Check the cookie hasn't expired.
  my $now = time();
  if ($now > $$cookie{UNTIL})
  {
    $r->log->notice("$me rejecting cookie for expiration"
	            . " '$$cookie{UNTIL}' vs. $now");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # Check we can decode the cookie payload.
  my $data = decode_auth_cookie($$cookie{DATA});
  if (! $data)
  {
    $r->log->warn("$me rejecting cookie for decode error '$$cookie{DATA}'");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # Verify user agent hasn't changed.
  my $user_agent = $r->headers_in->get('User-Agent') || '';
  if ($user_agent ne $$data{U})
  {
    $r->log->warn("$me rejeting cookie for user agent"
	          . " '$$data{U}' vs. '$user_agent'");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # Verify the account is valid.
  my $account = $$data{A};
  if ($account !~ m{^[a-z0-9]+(?:\.nocern|\.notcms)?$}
      || ! exists $authz_by_login{$account})
  {
    $r->log->warn("$me rejecting cookie for bad account '$account'");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # Reject revoked accounts.
  if (exists $revoked{LOGIN}{$account})
  {
    $r->log->warn("$me rejecting revoked account '$account'");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # Verify password hasn't changed.
  my $passkey = "$account $authz_by_login{$account}{PASSWD}";
  if (! secret_hmac_check("auth-pass", $passkey, $$data{P}))
  {
    $passkey = secret_hmac("auth-pass", $passkey);
    $r->log->warn("$me rejecting cookie for password change"
	          . " of '$account', got '$$data{P}' expected '$passkey'");
    $r->err_headers_out->add("Set-Cookie" => "cms-auth=$NULL_COOKIE");
    return authn_step($r, $opts);
  }

  # It is valid, accept it.
  $r->subprocess_env->set("AUTH_DONE" => "OK");
  $r->headers_in->set("CMS-Auth-Status" => "OK");
  $r->headers_in->set("CMS-Auth-" => $account);
  return authz_complete($ir, $r, $opts, METHOD => "HNLogin", LOGIN => $account);
}

# Create authentication cookie for Set-Cookie header. The arguments
# are cookie type, validity time, and two lists for keys and values.
# The type should be 'L' for login. The payload keys and values are
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
