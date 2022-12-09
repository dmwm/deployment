package testme;
use strict;
use warnings;
use Apache2::Const -compile => ':common', ':http';
use CGI 'param';

sub handler($)
{
  my ($r) = @_;
  $r->content_type('text/plain');
  $r->print("Environment:\n",
            (map { "$_ = $ENV{$_}\n" } sort keys %ENV), "\n",

            "Parameters:\n",
            (map { "$_ = @{[param($_)]}\n" } param()));

  return Apache2::Const::OK;
}

1;
