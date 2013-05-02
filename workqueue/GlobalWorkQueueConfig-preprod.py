#!/usr/bin/env python
"""
_GlobalWorkQueueConfig_

Global cmsweb-testbed WorkQueue config.
"""

import socket
import re
import os

from WMCore.Configuration import Configuration

workqueueDBName = 'workqueue'
workqueueInboxDbName = 'workqueue_inbox'
wmstatDBName = 'wmstats'
reqmgrCouchDB = "reqmgr_workload_cache"
HOST = "cmsweb-testbed.cern.ch"
REQMGR = "https://cmsweb-testbed.cern.ch/reqmgr/reqMgr"
COUCH = "https://cmsweb-testbed.cern.ch/couchdb"
WEBURL = "%s/%s" % (COUCH, workqueueDBName)
PHEDEX = "https://cmsweb-testbed.cern.ch/phedex/datasvc/json/prod/"

root = __file__.rsplit('/', 4)[0]
cache_dir = os.path.join(root, 'state', 'workqueue', 'cache')
os.environ['WMCORE_CACHE_DIR'] = cache_dir

# Nothing after this point should need to be changed.
config = Configuration()

config.section_("Agent")
config.Agent.hostName = HOST

config.component_("WorkQueueManager")
config.WorkQueueManager.namespace = "WMComponent.WorkQueueManager.WorkQueueManager"
config.WorkQueueManager.couchurl = COUCH
config.WorkQueueManager.dbname = workqueueDBName
config.WorkQueueManager.inboxDatabase = workqueueInboxDbName
config.WorkQueueManager.wmstatDBName = wmstatDBName
config.WorkQueueManager.level = "GlobalQueue"
config.WorkQueueManager.queueParams = {'WMStatsCouchUrl': "%s/%s" % (COUCH, wmstatDBName)}
config.WorkQueueManager.queueParams['PhEDExEndpoint'] = PHEDEX
config.WorkQueueManager.queueParams['QueueURL'] = WEBURL
config.WorkQueueManager.queueParams['ReqMgrServiceURL'] = REQMGR
config.WorkQueueManager.reqMgrConfig = {}
config.WorkQueueManager.reqMgrConfig['endpoint'] = REQMGR
