#!/usr/bin/env python2.6
from os import getenv
from json import loads, dump
from sys import argv, exit, stderr, stdout
from urllib2 import AbstractHTTPHandler, urlopen, \
                    build_opener, install_opener, HTTPError
from httplib import HTTPSConnection

class X509HTTPS(HTTPSConnection):
  def __init__(self, host, *args, **kwargs):
    HTTPSConnection.__init__(self, host, key_file = x509_proxy,
                             cert_file = x509_proxy, **kwargs)

class X509Auth(AbstractHTTPHandler):
  def default_open(self, req):
    return self.do_open(X509HTTPS, req)

def get_good_reqs(globalmon, cmsweb):
  doc = urlopen(globalmon+'monitorSvc/requestmonitor')
  reqs = loads(doc.read())
  good_status = ['running', 'acquired', 'assignment-approved', 'new', 'running-open', 'running-closed']
  good_reqs = []
  for r in reqs:
    workflow = r['request_name']
    status = r.get('status', None)
    if not status:
      print >>stderr, "Request "+workflow+" does not have status."
    elif status in good_status:
      try:
        doc = urlopen(cmsweb+'couchdb/reqmgr_workload_cache/'+workflow)
        r['details'] = loads(doc.read())
        doc = urlopen(cmsweb+'reqmgr/reqMgr/request/'+workflow)
        r['details2'] = loads(doc.read())
        doc = urlopen(cmsweb+'reqmgr/reqMgr/outputDatasetsByRequestName?requestName='+workflow)
        r['OutputDatasets'] = loads(doc.read())
        good_reqs.append(r)
      except HTTPError:
        # request not on the cache anymore
        print >>stderr, "Failed to fetch details for request "+workflow
        pass
  return good_reqs

if __name__ == '__main__':
  if len(argv) != 3:
    print >>stderr, 'Usage: %s <globalmonitor_base_url> <cmsweb_base_url> > output.json' % argv[0]
    print >>stderr, '  ex.: %s https://vocms204.cern.ch/reqmgr/' % argv[0], \
                    'https://cmsweb.cern.ch/ > output.json'
    exit(1)
  globalmon, cmsweb = argv[1:]

  x509_proxy = getenv("X509_USER_PROXY", None)
  if not x509_proxy:
    print >>stderr, "Proxy certificate not found."
    exit(1)

  opener = build_opener(X509Auth())  
  opener.addheaders = [('User-agent', 'Mozilla/5.0'), ('Accept', 'application/json')]
  install_opener(opener)
  
  dump(get_good_reqs(globalmon,cmsweb), stdout)
  exit(0)
