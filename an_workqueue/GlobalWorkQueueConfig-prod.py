#!/usr/bin/env python
"""
_GlobalWorkQueueConfig_

Global cmsweb WorkQueue config.
"""

import socket
import re
import os

from WMCore.Configuration import Configuration

workqueueDBName = 'analysis_workqueue'
workqueueInboxDbName = 'analysis_workqueue_inbox'
wmstatDBName = 'analysis_wmstats'
HOST = "cmsweb.cern.ch"
REQMGR = "https://cmsweb.cern.ch/an_reqmgr/reqMgr"
COUCH = "https://cmsweb.cern.ch/couchdb"
TEAMS = 'Analysis'
#TODO need to bettere understand how to handle teams for the analysis use case
#dataops,dmwm,integration,processing,production,relval,analysis,t1,t1_highprio,mc,mc_highprio'
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
config.WorkQueueManager.wmstatDBName = wmstatDBName
config.WorkQueueManager.inboxDatabase = workqueueInboxDbName
config.WorkQueueManager.level = "GlobalQueue"
config.WorkQueueManager.queueParams = {'WMStatsCouchUrl': "%s/%s" % (COUCH, wmstatDBName)}
config.WorkQueueManager.queueParams['QueueURL'] = WEBURL
config.WorkQueueManager.reqMgrConfig = {}
config.WorkQueueManager.reqMgrConfig['endpoint'] = REQMGR
