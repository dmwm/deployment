#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-
## CMS Web login needs XHTMLFormParser to work.
from mechanize import LinkNotFoundError, ItemNotFoundError
from Robot import init
import sys,optparse
import ConfigParser

config = ConfigParser.SafeConfigParser()
config.read('config.ini')

LINK_SECTION='SAVANNAH_URLS'
squads_page=config.get(LINK_SECTION, 'SQUADS_PAGE')


def main():
    parser = optparse.OptionParser()
    parser.add_option('--squadname', '-s', default="1")
    parser.add_option('--add', '-a',default=0)
    options, arguments = parser.parse_args()
    if(len(sys.argv)>=2):
        squad_name =options.squadname
        user_to_add=options.add
    else:
        sys.exit("No option passed. Aborting.")

    br = init() 
    print 'adding user with code %s to the squad %s'%(user_to_add, squad_name)
    try:
      br.open(squads_page)
      br.follow_link(text_regex=squad_name, nr=0)
      br.select_form(nr=3)
      br.form.set_all_readonly(False)
      br["user_id[]"]= [user_to_add]
      br.submit()
      print "added to squad"
    except LinkNotFoundError:
      print "squad does not exist.."
      exit(1)
    except ItemNotFoundError:
      print "user already in squad"
      exit(2)
    except Exception,e:
        print(e)
        exit(3)


if __name__ == '__main__':
    main()

