#!/usr/bin/env python
"""
_GlobalWorkQueueConfig_

Global WorkQueue config.
"""

import socket
import re
import os

from WMCore.Configuration import Configuration

workqueueDBName = 'analysis_workqueue'
workqueueInboxDbName = 'analysis_workqueue_inbox'
wmstatDBName = 'analysis_wmstats'
HOST = socket.getfqdn().lower()
REQMGR = "https://%s/an_reqmgr/reqMgr" % HOST
COUCH = "https://%s/couchdb" % HOST
TEAMS = 'Analysis'
WEBURL = "%s/%s" % (COUCH, workqueueDBName)


root = __file__.rsplit('/', 4)[0]
cache_dir = os.path.join(root, 'state', 'an_workqueue', 'cache')
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
config.WorkQueueManager.wmstatDBName = wmstatDBName
config.WorkQueueManager.level = "GlobalQueue"
config.WorkQueueManager.queueParams = {'WMStatsCouchUrl': "%s/%s" % (COUCH, wmstatDBName)}
config.WorkQueueManager.queueParams['QueueURL'] = WEBURL
config.WorkQueueManager.reqMgrConfig = {}
config.WorkQueueManager.reqMgrConfig['endpoint'] = REQMGR
