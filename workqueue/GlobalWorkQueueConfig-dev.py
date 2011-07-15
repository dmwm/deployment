#!/usr/bin/env python
"""
_GlobalWorkQueueConfig_

Global cmsweb-dev WorkQueue config.
"""

import socket
import re
import os

from WMCore.Configuration import Configuration

workqueueDBName = 'workqueue'
workqueueInboxDbName = 'workqueue_inbox'
HOST = "cmsweb-dev.cern.ch"
REQMGR = "https://cmsweb-dev.cern.ch/reqmgr/reqMgr"
COUCH = "https://cmsweb-dev.cern.ch/couchdb"
TEAMS = 'TestTeam'
WEBURL = "https://cmsweb-dev.cern.ch/workqueue"


root = __file__.rsplit('/', 4)[0]
cache_dir = os.path.join(root, 'state', 'workqueue', 'cache')
os.environ['WMCORE_CACHE_DIR'] = cache_dir

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
