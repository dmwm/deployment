#!/usr/bin/env python
#-*- coding: utf-8 -*-

import ConfigParser

config = ConfigParser.SafeConfigParser()
config.read('config.ini')

# getfloat() raises an exception if the value is not a float
# getint() and getboolean() also do this for their respective types
site= config.get('SAVANNAH_URLS', 'SITE')
login=config.get('SAVANNAH_URLS', 'LOGIN_PAGE')
create_site=config.get('SAVANNAH_URLS','CREATE_SITE')
FORMATTER=config.get('LOGGING','FORMATTER')
print FORMATTER
print create_site
print login
print site
