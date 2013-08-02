#!/usr/bin/env python

## CMS Web login needs XHTMLFormParser to work.

## make a new DefaultFactory
#from ClientForm import XHTMLCompatibleFormParser

from SiteDB import getSiteDBSiteNames
import optparse
import sys
import re
def main():
    parser = optparse.OptionParser()
    parser.add_option('--output', '-O', default="out.txt")
    options, arguments = parser.parse_args()
    if(len(sys.argv)>=2):
        pass
    else:
        sys.exit("None output file passed. Aborting.")

    site_names= getSiteDBSiteNames()
    site_names= [x for x in site_names if re.match('T[0-3]_*',x[1])<>None]
#    site_names= [x for x in site_names if re.match('T3_*',x[1])<>None]
    k=0
    f=open(options.output, 'w')
    for k in range(len(site_names)):
        f.write('%s\n'%(site_names[k][1]))
    f.close()

if __name__ == '__main__':
    main()
