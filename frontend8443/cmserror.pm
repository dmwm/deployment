package cmserror;
use strict;
use warnings;
use Apache2::Util;
use Apache2::Const -compile => ':common', ':http';
use cmstools;

my $errdoc = <<'END_OF_ERROR';
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
 <head>
 <title>CMSWEB Error: {TITLE}</title>
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
    <h2>{TITLE}</h2>
    {MESSAGE}
   </div>
  </div>
  <div id="bottom">
   <div class="boxFooter">&nbsp;</div>
  </div>
 </div>
</body>
</html>
END_OF_ERROR

sub handler($)
{
  my ($r) = @_;
  my $err = $r->path_info();
  my $title = "Unexpected error occurred";
  my $message = "<p>An unspecified error occurred.</p>";
  my $ticket = "please be so kind and <a href='https://ggus.eu/?"
             . "mode=ticket_cms'>create a ticket</a> to"
             . "\"CMS Web Tools\" support unit</a>";

  if ($err eq "/401")
  {
    $title = "Internal server configuration error";
    $message = "<p>The site you accessed requests unexpected authorisation"
             . " method. Would you $ticket?</p>";
  }
  elsif ($err eq "/403")
  {
    # my $auth = $r->subprocess_env("AUTH_SPEC");
    # my $rauth = $r->subprocess_env("REDIRECT_AUTH_SPEC");
    my $ir = initialreq($r);
    my $uri = Apache2::Util::escape_path($ir->unparsed_uri(), $r->pool);
    $uri =~ s/'/%27/g;

    $title = "Authorisation required";
    $message = "<p>The site you requested is protected and requires you"
             . " to authenticate</p><p><a href='/auth/trouble'>Diagnose"
             . " certificate problems</a></p>";
  }
  elsif ($err eq "/404")
  {
    $title = "No such site";
    $message = "<p>The site you requested does not exist."
             . " Could we interest you in <a href='/'>anything else</a>?</p>";
  }
  elsif ($err eq "/503")
  {
    $title = "Service unavailable";
    $message = "<p>The site you requested is not available.</p>"
	     . "<p>CMS <a href='https://twiki.cern.ch/twiki/bin/view/CMS/"
	     . "ScheduledInterventions'>scheduled interventions page</a> lists"
	     . " planned CMS and CERN service downtimes and known site-wide"
	     . " computing system incidents. Planned updates are notified on"
	     . " the <a href='https://hypernews.cern.ch/HyperNews/CMS/get/"
	     . "cernCompAnnounce.html'>CERN computing announcements</a> forum.</p>"
	     . "<p>Would you $ticket if this interruption was unexpected?</p>";
  }

  my $body = $errdoc;
  $body =~ s/\{TITLE\}/$title/g;
  $body =~ s/\{MESSAGE\}/$message/g;

  $r->content_type('text/html');
  $r->print($body);
  return Apache2::Const::OK;
}

1;
