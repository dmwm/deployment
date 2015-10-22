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

HOST = socket.getfqdn().lower()
if re.match(r"^vocms0127\.cern\.ch$", HOST):
  ALIAS = "cmsweb-dev.cern.ch"
elif re.match(r"^vocms0126\.cern\.ch$", HOST):
  ALIAS = "cmsweb-sec.cern.ch"
else:
  ALIAS = HOST

REQMGR = "https://%s/reqmgr/reqMgr" % ALIAS
REQMGR2 = "https://%s/reqmgr2" % ALIAS
COUCH = "https://%s/couchdb" % ALIAS
WEBURL = "%s/%s" % (COUCH, workqueueDBName)
LOG_DB_URL = "%s/wmstats_logdb" % COUCH
LOG_REPORTER = "global_workqueue"

root = __file__.rsplit('/', 4)[0]
cache_dir = os.path.join(root, 'state', 'workqueue', 'cache')
os.environ['WMCORE_CACHE_DIR'] = cache_dir

# Nothing after this point should need to be changed.
config = Configuration()

config.section_("Agent")
config.Agent.hostName = ALIAS

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
config.WorkQueueManager.queueParams['RequestDBURL'] = "%s/%s" % (COUCH, reqmgrCouchDB)
config.WorkQueueManager.queueParams['central_logdb_url'] = LOG_DB_URL
config.WorkQueueManager.queueParams['log_reporter'] = LOG_REPORTER
config.WorkQueueManager.reqMgrConfig = {}
config.WorkQueueManager.reqMgrConfig['endpoint'] = REQMGR
# when reqmgr2 is ready change following to endpoint and reqmgr2_only to True
config.WorkQueueManager.reqMgrConfig['reqmgr2_endpoint'] = REQMGR2
config.WorkQueueManager.reqMgrConfig['reqmgr2_only'] = False
config.WorkQueueManager.reqMgrConfig['central_logdb_url'] = LOG_DB_URL
config.WorkQueueManager.reqMgrConfig['log_reporter'] = LOG_REPORTER
