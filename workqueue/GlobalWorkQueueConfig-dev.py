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
wmstatDBName = 'wmstats'
reqmgrCouchDB = "reqmgr_workload_cache"
HOST = "cmsweb-dev.cern.ch"
REQMGR = "https://cmsweb-dev.cern.ch/reqmgr/reqMgr"
REQMGR2 = "https://%s/reqmgr2" % HOST
COUCH = "https://cmsweb-dev.cern.ch/couchdb"
WEBURL = "%s/%s" % (COUCH, workqueueDBName)


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
config.WorkQueueManager.queueParams['QueueURL'] = WEBURL
config.WorkQueueManager.queueParams['ReqMgrServiceURL'] = REQMGR2
config.WorkQueueManager.reqMgrConfig = {}
config.WorkQueueManager.reqMgrConfig['endpoint'] = REQMGR
# when reqmgr2 is ready change following to endpoint and reqmgr2_only to True
config.WorkQueueManager.reqMgrConfig['reqmgr2_endpoint'] = REQMGR2
config.WorkQueueManager.reqMgrConfig['reqmgr2_only'] = False
