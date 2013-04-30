#!/usr/bin/env python
"""
_ACDCConfig_

ACDC config for a development deployment
"""
from WMCore.Configuration import Configuration

acdcDatabase = "acdcserver"
HOST = "cmsweb-dev.cern.ch"
COUCH = "https://%s/couchdb" % HOST

# Nothing after this point should need to be changed.
config = Configuration()

config.section_("Agent")
config.Agent.hostName = HOST

config.component_("ACDC")
config.ACDC.couchurl = COUCH
config.ACDC.dbname = acdcDatabase
config.ACDC.cleaningInterval = 30
