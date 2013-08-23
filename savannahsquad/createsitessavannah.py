#!/usr/bin/env python

## CMS Web login needs XHTMLFormParser to work.

## make a new DefaultFactory
from mechanize import XHTMLCompatibleFormParser
from mechanize._html import DefaultFactory,FormsFactory
from mechanize import Browser
import pprint
import sys, re, os

from SiteDB import getSiteDBSiteNames

login_page='https://savannah.cern.ch/account/login.php?uri=%2F'
create_site='https://savannah.cern.ch/support/admin/field_values.php?group=cmscompinfrasup&list_value=1&field=custom_sb1'
#site_list='https://cmsweb.cern.ch/sitedb/reports/showReport?reportid=naming_convention.ini'
new_form_fac=FormsFactory(form_parser_class=XHTMLCompatibleFormParser)
new_def_fac=DefaultFactory()
new_def_fac._forms_factory=new_form_fac
br=Browser(factory=new_def_fac)

#br.set_handle_referer(True)
br.set_handle_refresh(True)
#br.set_handle_equiv(True)

## HTTP Error 403: request disallowed by robots.txt
br.set_handle_robots(False)

#lets get a list of CMS names from SiteDB
label="Getting site names from SiteDB".ljust(50,'.')
sys.stdout.write(label[0:40])
sys.stdout.flush()
siteNamesFromSiteDB = getSiteDBSiteNames()

siteNamesFromSiteDB=[x[1] for x in siteNamesFromSiteDB]
for site in siteNamesFromSiteDB:
  if site.endswith('_Disk'):
    siteNamesFromSiteDB.remove(site)

totalNames = len(siteNamesFromSiteDB)

if totalNames==0:
  sys.stdout.write('   Error: site names not fetched - Aborting')
  sys.stdout.flush()
  exit(2)

sys.stdout.write('   Ok  (%d names fetched from SiteDB)\n'%totalNames)
sys.stdout.flush()

#print siteNamesFromSiteDB

#Now we have our CMS names list, go to login page
label="Fetching squads already at Savannah".ljust(50,'.')
sys.stdout.write(label[0:40])
sys.stdout.flush()

try:
  br.open(login_page)
  ## 'Search' form is form 0
  ## login form is form 1
  br.select_form(nr=1)
  f = open(os.environ['PASSWD_FILE'], 'r')
  passwd=f.readline()
  f.close()

  br['form_loginname']='sitedbrobot'
  br['form_pw']=passwd.replace('\n','')
  br.submit()
  br.open(create_site)
except Exception,e:
  sys.stdout.write('   Error: %s - aborting\n'%e)
  sys.stdout.flush()
  exit(2)

# fetch all site squads from savannah
squadLists=br.response().read()

onlyActiveSquads=re.search('---- ACTIVE VALUES ----.*---- HIDDEN VALUES ----',squadLists,re.DOTALL)
onlyActiveSquads=onlyActiveSquads.group()

findSquadsRegex = re.compile(re.escape('&field=custom_sb1&group_id=452">')
                  + '(T[0123].*?)'
                  + re.escape('</A></td><td>')
                  + '(.*?)'
                  + re.escape('&nbsp;</td><td align="center">')
                  + '(.*?)'
                  + re.escape('</td><td align="center">')
                  + '(.*?)'
                  + re.escape('</td><td align="center">')
                  + '(.*?)'
                  + re.escape('</td></tr>'), re.I | re.S | re.M)

activeSquads = re.findall(findSquadsRegex,onlyActiveSquads)
totalSquads=len(activeSquads)

if totalSquads==0:
  sys.stdout.write('   Error: squad names not fetched from Savannah - Aborting')
  sys.stdout.flush()
  exit(2)

sys.stdout.write('   Ok  (%d squads fetched from Savannah)\n'%totalSquads)
sys.stdout.flush()


siteNamesFromSavannah=[x[0] for x in activeSquads]
siteNamesFromSavannah=sorted(siteNamesFromSavannah)

label="SiteDB x Savannah".ljust(50,'.')
sys.stdout.write(label[0:40])
sys.stdout.flush()
diff=set(siteNamesFromSiteDB).difference(siteNamesFromSavannah)
squadsToCreate=list(diff)

if len(squadsToCreate)==0:
  sys.stdout.write("   Ok\n")
else:
  sys.stdout.write("   Error. The following sites are in SiteDB but not in Savannah:\n")
  print squadsToCreate

label="Savannah x SiteDB".ljust(50,'.')
sys.stdout.write(label[0:40])
sys.stdout.flush()

diff=set(siteNamesFromSavannah).difference(siteNamesFromSiteDB)
diff=list(diff)
if len(diff)==0:
  sys.stdout.write("   Ok\n")
else:
  sys.stdout.write("   Warning. The following sites are in Savannah but not in SiteDB:\n")
  print diff

if len(squadsToCreate)==0:
  print "No site/squad needs to be created"
  exit(0)


print "Creating site"
sys.stdout.write("       %s"%"Site".ljust(40,' '))
sys.stdout.write("Rank\n")

for squad in squadsToCreate:
  #find the last Rank from a given country
  squadsForCountry=[x for x in activeSquads if squad[0:5] in x[0]]
  if len(squadsForCountry) == 0:
    # no squads found for this country
    lastRank=str(int(activeSquads[-1][2])+5)
  else:
    # last squad for this site
    lastRank=squadsForCountry[-1][2]

  try:
    br.select_form(nr=1)
    br.form.set_all_readonly(False)
    br['title']=squad
    br['order_id']= lastRank
    br['description']='Created by SiteDB robot'
    br.submit()
    br.open(create_site)
    label=squad.ljust(40,' ')
    sys.stdout.write("       %s"%label[0:40])
    sys.stdout.write("%s\n"%lastRank)
    sys.stdout.flush()
  except Exception,e:
    sys.stdout.write('   Error: %s - Aborting\n'%e)
    sys.stdout.flush()
    exit(1)


