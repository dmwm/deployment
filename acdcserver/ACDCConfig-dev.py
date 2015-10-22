#!/usr/bin/env python
"""
_ACDCConfig_

ACDC config for a development deployment
"""
import socket
from WMCore.Configuration import Configuration

acdcDatabase = "acdcserver"

HOST = socket.getfqdn().lower()
if re.match(r"^vocms0127\.cern\.ch$", HOST):
  ALIAS = "cmsweb-dev.cern.ch"
elif re.match(r"^vocms0126\.cern\.ch$", HOST):
  ALIAS = "cmsweb-sec.cern.ch"
else:
  ALIAS = HOST
COUCH = "https://%s/couchdb" % ALIAS

# Nothing after this point should need to be changed.
config = Configuration()

config.section_("Agent")
config.Agent.hostName = ALIAS

config.component_("ACDC")
config.ACDC.couchurl = COUCH
config.ACDC.dbname = acdcDatabase
config.ACDC.cleaningInterval = 30
