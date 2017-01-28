"""
_GlobalWorkQueueConfig_

Global cmsweb WorkQueue config.
"""

import socket
import os
import time

from WMCore.Configuration import Configuration

workqueueDBName = 'workqueue'
workqueueInboxDbName = 'workqueue_inbox'
wmstatDBName = 'wmstats'
reqmgrCouchDB = "reqmgr_workload_cache"

HOST = socket.gethostname().lower()
BASE_URL = "@@BASE_URL@@"
DBS_INS = "@@DBS_INS@@"
COUCH_URL = "%s/couchdb" % BASE_URL

REQMGR2 = "%s/reqmgr2" % BASE_URL
WEBURL = "%s/%s" % (COUCH_URL, workqueueDBName)
LOG_DB_URL = "%s/wmstats_logdb" % COUCH_URL
LOG_REPORTER = "global_workqueue"

root = __file__.rsplit('/', 4)[0]
cache_dir = os.path.join(root, 'state', 'workqueue', 'cache')
os.environ['WMCORE_CACHE_DIR'] = cache_dir

ROOTDIR = __file__.rsplit('/', 3)[0]
config = Configuration()

# this section is only needed for updating couchapp (it is using wmagent-couchapp-init)
config.section_("WorkQueueManager")
config.WorkQueueManager.couchurl = COUCH_URL
config.WorkQueueManager.dbname = workqueueDBName
config.WorkQueueManager.inboxDatabase = workqueueInboxDbName

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "globalworkqueue"
main.application_dir = "workqueue"
main.port = 8240 # main application port it listens on (TODO: temporary port updated as Bruno advises)
main.index = "ui"
# Defaults to allow any CMS authenticated user. Write APIs should require
# additional roles in SiteDB (i.e. "Admin" role for the "ReqMgr" group)
main.authz_defaults = {"role": None, "group": None, "site": None}

sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application) # string containing "globalworkqueue"
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS data operations Global WorkQueue"
app.title = " Global WorkQueue (GQ)"

views = config.section_("views")

def setWorkQueueCommonConfig(config):    
    # actual params need to creaating global queue
    config.queueParams = {}
    config.queueParams['CouchUrl'] = COUCH_URL
    config.queueParams['DbName'] = workqueueDBName
    config.queueParams['InboxDbName'] = workqueueInboxDbName
    config.queueParams['WMStatsCouchUrl'] = "%s/%s" % (COUCH_URL, wmstatDBName)
    config.queueParams['QueueURL'] = WEBURL
    config.queueParams['ReqMgrServiceURL'] = REQMGR2
    config.queueParams['RequestDBURL'] = "%s/%s" % (COUCH_URL, reqmgrCouchDB)
    config.queueParams['central_logdb_url'] = LOG_DB_URL
    config.queueParams['log_reporter'] = LOG_REPORTER
    
    config.reqMgrConfig = {}
    config.reqMgrConfig['reqmgr2_endpoint'] = REQMGR2
    config.reqMgrConfig['central_logdb_url'] = LOG_DB_URL
    config.reqMgrConfig['log_reporter'] = LOG_REPORTER

# Production instance of globalworkqueue, must be a production back-end
if HOST.startswith("vocms0140") or HOST.startswith("vocms0131") or HOST.startswith("vocms0127"):
    extentions = config.section_("extensions")
    reqmgrInteraction = extentions.section_("reqmgrInteraction")
    reqmgrInteraction.object = "WMCore.GlobalWorkQueue.CherryPyThreads.ReqMgrInteractionTask.ReqMgrInteractionTask"
    setWorkQueueCommonConfig(reqmgrInteraction)
    reqmgrInteraction.interactDuration = 60 * 5 # every 5 minutes
    reqmgrInteraction.log_file = '%s/logs/workqueue/reqmgrInteractionTask-%s.log' % (__file__.rsplit('/', 4)[0], time.strftime("%Y%m%d"))
    reqmgrInteraction.central_logdb_url = LOG_DB_URL
    reqmgrInteraction.log_reporter = LOG_REPORTER
    
    # location update
    locationUpdateTask = extentions.section_("locationUpdateTask")
    locationUpdateTask.object = "WMCore.GlobalWorkQueue.CherryPyThreads.LocationUpdateTask.LocationUpdateTask"
    setWorkQueueCommonConfig(locationUpdateTask)
    locationUpdateTask.locationUpdateDuration = 60 * 20 # every 20 minutes
    locationUpdateTask.log_file = '%s/logs/workqueue/locationUpdateTask-%s.log' % (__file__.rsplit('/', 4)[0], time.strftime("%Y%m%d"))
    locationUpdateTask.central_logdb_url = LOG_DB_URL
    locationUpdateTask.log_reporter = LOG_REPORTER
    
    # workqueue cleanup threads
    cleanUpTask = extentions.section_("cleanUpTask")
    cleanUpTask.object = "WMCore.GlobalWorkQueue.CherryPyThreads.CleanUpTask.CleanUpTask"
    setWorkQueueCommonConfig(cleanUpTask)
    cleanUpTask.cleanUpDuration = 60 * 10 # every 10 minutes
    cleanUpTask.log_file = '%s/logs/workqueue/cleanUpTask-%s.log' % (__file__.rsplit('/', 4)[0], time.strftime("%Y%m%d"))
    cleanUpTask.central_logdb_url = LOG_DB_URL
    cleanUpTask.log_reporter = LOG_REPORTER
    
    # workqueue monitoring thread
    monitTask = extentions.section_("monitTask")
    monitTask.object = "WMCore.GlobalWorkQueue.CherryPyThreads.MonitoringTask.MonitoringTask"
    setWorkQueueCommonConfig(monitTask)
    monitTask.monitDuration = 60 * 30 # every 30 minutes
    monitTask.log_file = '%s/logs/workqueue/monitTask-%s.log' % (__file__.rsplit('/', 4)[0], time.strftime("%Y%m%d"))
    monitTask.central_logdb_url = LOG_DB_URL
    monitTask.log_reporter = LOG_REPORTER