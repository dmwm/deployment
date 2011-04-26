#!/usr/bin/env python
"""
_GlobalWorkQueueConfig_

Global WorkQueue config.
"""

import socket
import re

from WMCore.Configuration import Configuration

workqueueDBName = 'workqueue'
workqueueInboxDbName = 'workqueue_inbox'
HOST = socket.getfqdn().lower()
REQMGR = "https://%s/reqmgr/reqMgr" % HOST
COUCH = "http://localhost:5984"
TEAMS = 'cmsdataops'
WEBURL = "%s/%s" % (COUCH, workqueueDBName)

# Apply host specific configuration
if re.match(r"^vocms(?:10[67]|5[03])\.cern\.ch$", HOST):
  HOST = "cmsweb.cern.ch"
  REQMGR = "https://cmsweb.cern.ch/reqmgr/reqMgr"
  WEBURL = "https://cmsweb.cern.ch/workqueue"
elif re.match(r"^vocms(?:51|13[23])\.cern\.ch$", HOST):
  HOST = "cmsweb-testbed.cern.ch"
  REQMGR = "https://cmsweb-testbed.cern.ch/reqmgr/reqMgr"
  WEBURL = "https://cmsweb-testbed.cern.ch/workqueue"


# Nothing after this point should need to be changed.
config = Configuration()

config.section_("Agent")
config.Agent.hostName = HOST
config.Agent.teamName = TEAMS

config.component_("WorkQueueManager")
config.WorkQueueManager.namespace = "WMComponent.WorkQueueManager.WorkQueueManager"
config.WorkQueueManager.couchurl = COUCH
config.WorkQueueManager.dbname = workqueueDBName
config.WorkQueueManager.inboxDatabase = workqueueInboxDbName
config.WorkQueueManager.level = "GlobalQueue"
config.WorkQueueManager.queueParams = {}
config.WorkQueueManager.queueParams['QueueURL'] = WEBURL
config.WorkQueueManager.reqMgrConfig = {}
config.WorkQueueManager.reqMgrConfig['endpoint'] = REQMGR
