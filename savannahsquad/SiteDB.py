#!/usr/bin/env python
"""
Old sitedb reports from sitedb v2
"""

import urllib
import json
import unicodedata
from pprint import pprint

SITE_ADMINS=''

def myOpener(url):
  # build a custom opener to use a cert proxy to authenticate
  opener = urllib.URLopener(key_file = './proxy.pem', cert_file = './proxy.pem')
  # change HTTP Accept header to fetch json instead XML
  opener.addheader('Accept', 'application/json')
  response = opener.open(url)
  return response

def getSiteDBSiteNames():
  url = 'https://cmsweb.cern.ch/sitedb/data/prod/site-names'
  response = myOpener(url)
  the_page = response.read()
  ajson = json.loads(the_page)
  cms_sites = [(unicodedata.normalize('NFKD', x[1]).encode('ascii','ignore'), 
                unicodedata.normalize('NFKD', x[2]).encode('ascii','ignore')) 
                   for x in ajson['result'] if x[0] == 'cms']
  cms_sites = sorted(cms_sites)

  return cms_sites

def getLCGSiteNames():
  url = 'https://cmsweb.cern.ch/sitedb/data/prod/site-names'
  response = myOpener(url)
  the_page = response.read()
  ajson = json.loads(the_page)
  lcg_sites = [(unicodedata.normalize('NFKD', x[1]).encode('ascii','ignore'),
                unicodedata.normalize('NFKD', x[2]).encode('ascii','ignore'))
                   for x in ajson['result'] if x[0] == 'lcg']
  lcg_sites = sorted(lcg_sites)

  return lcg_sites

def getPeople(user):
  url = 'https://cmsweb.cern.ch/sitedb/data/prod/people?match=%s'%user
  response = myOpener(url)
  the_page = response.read()
  allPeople = json.loads(the_page)
  thePeople = [x for x in allPeople['result'] if x[0] == user ]

  people = [(unicodedata.normalize('NFKD',x[2]).encode('ascii','ignore'), 
             unicodedata.normalize('NFKD',x[3]).encode('ascii','ignore'),
             unicodedata.normalize('NFKD',x[1]).encode('ascii','ignore'))
               for x in thePeople] 

  return people

def getCMSNamesToAdmin(siteName):
  global SITE_ADMINS
  if SITE_ADMINS == '':
    url = 'https://cmsweb.cern.ch/sitedb/data/prod/site-responsibilities'
    response = myOpener(url)
    the_page = response.read()
    SITE_ADMINS = json.loads(the_page)

  admins = [ unicodedata.normalize('NFKD', x[0]).encode('ascii','ignore') 
               for x in SITE_ADMINS['result'] if x[1] == siteName]
  #pprint(SITE_ADMINS)
  admins = sorted(set(admins))
  infoReturn = []
  for admin in admins:
    userinfo = getPeople(admin)
    #print(userinfo)
    infoReturn.append(userinfo[0])


  return infoReturn

def getSiteExecutives():
  global SITE_ADMINS
  if SITE_ADMINS == '':
    url = 'https://cmsweb.cern.ch/sitedb/data/prod/site-responsibilities'
    response = myOpener(url)
    the_page = response.read()
    SITE_ADMINS = json.loads(the_page)

  executives = [ (unicodedata.normalize('NFKD', x[0]).encode('ascii','ignore'),
                  unicodedata.normalize('NFKD', x[1]).encode('ascii','ignore'))
                    for x in SITE_ADMINS['result'] if x[2] == 'Site Executive']
  #pprint(SITE_ADMINS)
  executives = sorted(set(executives))
  return executives

def main():
  lcg=getLCGSiteNames()
  cms=getSiteDBSiteNames()
  cmsandlcg = []
  for cms_name in cms:
     found=0 
     for lcg_name in lcg:
       if cms_name[0] == lcg_name[0]:
          #cmsandlcg.append([cms_name[0],cms_name[1],lcg_name[1]])
          found=1
          break
     if found == 0:
          cmsandlcg.append([cms_name[0],cms_name[1],"NONE"])     
            
       

  pprint(cmsandlcg)
         
  exit(0) 
  admins = getCMSNamesToAdmin('GRIF_IRFU') 
  pprint(SITE_ADMINS)
  exit(0)

  print admins
  #print  getSiteDBSiteNames()
  exit(0)
 
  print "  %s" % admins
  for admin in admins:
    userinfo = getPeople(admin)
    print userinfo

if __name__ == '__main__':
    main()

