# Module to clean off dangerous headers from incoming requests.
#
# We don't want the incoming request to set any headers for proxying,
# nor anything that this server sets internally, especially authn or
# authz related.
#
# A lot could be done with with simple "RequestHeader unset X"
# at the server config level, but this module adds capability to
# warn about when that happens, and does the clean-up only on the
# first incoming request to avoid touching headers set inside the
# processing (e.g. auth module, ssl headers).
package cmsnuke;
use strict;
use warnings;
use Apache2::Const 'DECLINED';

# for x509-scitoken-issuer we relax pattern in order to pass CMS headers to it
#my $bad_hdr = qr{^(?:via|x-forwarded-|cms-|ssl_|https)}io;
my $bad_hdr = qr{^(?:via|x-forwarded-|https)}io;

sub handler($)
{
  my ($r) = @_;

  # Do work only on first incoming request.
  if (! $r->prev)
  {
    foreach (grep /$bad_hdr/, keys %{$r->headers_in})
    {
      $r->log->warn("clearing incoming request header $_");
      $r->headers_in->unset($_);
    }
  }

  return Apache2::Const::DECLINED;
}

1;
