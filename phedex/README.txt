This document describes how to set up the web server.

* Overview

There are PhEDEx instances, each with an associated database (TMDB).
Separately there is a PhEDEx web site, which allows clients to look
into what is happening in the databases.  A single web service can
show the status of any number of PhEDEx database instances.

The web service serves only a small number of static files, most of
the content is dynamically generated from the state of the PhEDEx
database instance by a CGI script.  The operation of the web service
depends on a number of PhEDEx service agents running somewhere else.
This is because the web site rarely displays the true state of the
full database, the queries would be far too expensive; and of course
it would not be able to show historical information.  The PhEDEx
service agents monitor the state of the entire system and make the
current and historical metrics available for quick access by the web
service.

There should be two separate web service locations, one for the
production use and another for testing and development.  Normally both
services would serve the same set of databases, the test one possibly
adding development databases.  It is possible to host both services in
different directories on the same server.

* Security

The secure portions of the site are expected to be accessed with https
authenticated using the grid certificate of a person signed up to be a
PhEDEx administrator.  The https negotiation can be done either by the
server hosting the site, or by a front-end proxy server.  In the
latter case the configuration needs to be done with extreme care to
avoid opening security holes.  The standard service at CERN operates
behind a proxy.

* Server configuration overview

The PhEDEx web server is designed to run under Apache and mod_perl.
It is no doubt possible to make it work under other configurations,
only we have not tested any.  In theory mod_perl could be avoided, but
it is essential for a pleasant user experience.

The site is accessed via a proxy-only server set up by configured by
the CMS WEBTOOLS group, which hands the actual requests to a back end
server.  We describe the configurations for both.

The front-end server runs Apache 2.2.x on a Linux system which is
built, packaged, and configured by the CMS WEBTOOLS group.  For the
insecure part, it just does the normal proxy for the service URL using
"RewriteRule ... [P,L]" rules.  The secure part does SSL negotiation
with optional client verification, matching the user's certificate
public key against the grid certificate authority certificates (CA
certs).  The results of the user verification are passed to the back
end server in extra HTTP header parameters.

In the front end server, the SSL client verification is restricted
inside the PhEDEx service <Location>, i.e. it's not global to the
whole server -- asking all secure access to cmsdoc.cern.ch to present
a certificate would be inappropriate.  This means that at protocol
level a SSL re-negotiation is triggered.  Due to various Apache bugs
and security concerns in the interactions of buffering POST requests
and the SSL session re-negotiation, it is mandatory to use Apache 2.2
at least for the secure part of the web.  To our knowledge there is
no way to get Apache 2.0.x to work reliably.

The back end server runs on the same architecture as the front end.
The system mod_perl however is not usable, it is an odd RedHat hybrid
of mod_perl versions 1 and 2.  Instead, mod_perl was packaged into a
CMS-style RPM for deployment using the usual methods.  The backend
Apache is configured to use a high port number (default 7102) and
accept only connections from the front end server.  For even more
security the system firewall should be configured to only accept
connections from the front end server.

* Front end server configuration

(Note: This topic is now under the responsibility of the CMS WEBTOOLS
group.  This section is kept to describe the previous configuration,
in case it is useful information.)

The front end needs the following proxy redirect rule, assuming the
back end server is cmslcgco03 and expects the same URL structure as
the front-end:

  RewriteEngine  on
  RewriteRule ^(/cms(/test)?/aprom/phedex.*) http://cmslcgco03$1 [P,L]

For the secure part the above needs to be preceded by the following
in the <VirtualHost> for port 443, in addition to standard SSL stuff:

  # Grid CA certificates for authentication
  SSLCACertificateFile  /etc/httpd/conf/ca-bundle-client.crt
  SSLCARevocationFile /etc/httpd/conf/ca-bundle-revocation.crl

  # Pass SSL_CLIENT_CERT, SSL_CLIENT_S_DN, SSL_CLIENT_VERIFY
  # into the proxy request to the back-end server.
  RequestHeader set SSL_CLIENT_CERT %{SSL_CLIENT_CERT}e
  RequestHeader set SSL_CLIENT_S_DN %{SSL_CLIENT_S_DN}e
  RequestHeader set SSL_CLIENT_VERIFY %{SSL_CLIENT_VERIFY}e
  RequestHeader set HTTPS %{HTTPS}e

  # Require authentication to the PhEDEx service
  <LocationMatch ~ "^/cms(/test)?/aprom/phedex">
    SSLRequireSSL
    SSLVerifyDepth 1
    SSLVerifyClient optional
    SSLOptions +StdEnvVars +StrictRequire +CompatEnvVars +ExportCertData
    SSLRequire %{SSL_CIPHER_USEKEYSIZE} >= 128
  </LocationMatch>

Note that you should not use "SSLVerifyClient require", or restrict
proxy to only pass through successful authentications.  The back end
takes care of that gracefully using the additional headers.

Here, /etc/httpd/conf/ca-bundle-client.crt is the combination of all
the grid CA certificate public keys, and should be automatically
updated as the public keys are on any grid user interface system.
The file can be generated simply with:

  gridcerts=/etc/grid-security/certificates # (where ever they are)
  cat $gridcerts/*.[0-9] > /etc/httpd/ssl/ca-bundle-client.crt

The /etc/httpd/conf/ca-bundle-revocation.crl needs to be updated
automatically similarly for the list of revoked grid certificates.
[FIXME: instructions to generate the file!]

Make sure httpd is automatically started on system startup.

* Back end server configuration

** System setup

Change the firewall to accept connections only from the proxy server.
This is a highly recommended additional security measure.  Doing so
prevents anyone from even attempting to spoof the HTTPS parameters
passed by the front end server to the back end in extra headers.

** Instal PhEDEx website RPMs

The PhEDEx website RPM contains a default configuration which can be
run with few changes after installation.  Installing the website RPM
also installs all required dependencies, including Apache 2.2.x, if it
is not already available the software area.

[FIXME:  describe how to install and run from the RPMs]
[  Basic instructions:
   1.  Install the RPMs for PHEDEX-web and PHEDEX-graphtool, as well as WEBTOOLS
   2.  Copy the startup.sh script from PHEDEX-web to apache2-conf/startup.d
   3.  Copy the phedexweb-httpd.conf to apache2-conf/apps.d
   4.  Start apache.  (./apache2-conf/bin/httpd -k start)
]
