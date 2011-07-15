#!/usr/bin/env python
"""
_GlobalWorkQueueConfig_

Global WorkQueue config.
"""

import socket
import re
import os

from WMCore.Configuration import Configuration

workqueueDBName = 'workqueue'
workqueueInboxDbName = 'workqueue_inbox'
HOST = socket.getfqdn().lower()
REQMGR = "https://%s/reqmgr/reqMgr" % HOST
COUCH = "https://%s/couchdb" % HOST
TEAMS = 'TestTeam'
WEBURL = "%s/%s" % (COUCH, workqueueDBName)


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
