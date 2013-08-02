#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-
## CMS Web login needs XHTMLFormParser to work.

## make a new DefaultFactory
from mechanize import XHTMLCompatibleFormParser
from mechanize._html import DefaultFactory,FormsFactory
from mechanize import Browser,LinkNotFoundError
import ConfigParser

config = ConfigParser.SafeConfigParser()
config.read('config.ini')


LINK_SECTION='SAVANNAH_URLS'
login_page=config.get(LINK_SECTION,'LOGIN_PAGE')

def init():
    new_form_fac=FormsFactory(form_parser_class=XHTMLCompatibleFormParser)
    new_def_fac=DefaultFactory()
    new_def_fac._forms_factory=new_form_fac
    br=Browser(factory=new_def_fac)

    #br.set_handle_referer(True)
    br.set_handle_refresh(True)
    #br.set_handle_equiv(True)

    ## HTTP Error 403: request disallowed by robots.txt
    br.set_handle_robots(False)
    br.open(login_page)

    ## 'Search' form is form 0
    ## login form is form 1
    br.select_form(nr=1)
    #br.form.set_all_readonly(False)
    #reading from my_secret.txt
    f = open('my_secret.txt', 'r')
    passwd=f.readline()
    f.close()
    br['form_loginname']='sitedbrobot'
    br['form_pw']=passwd.replace('\n','')
    br.submit()
    return br

