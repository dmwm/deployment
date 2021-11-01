"""
_GlobalWorkQueueConfig_

Global cmsweb WorkQueue config.
"""
from __future__ import print_function

import socket
import os
import time
import sys
from WMCore.Configuration import Configuration

workqueueDBName = 'workqueue'
workqueueInboxDbName = 'workqueue_inbox'
wmstatDBName = 'wmstats'
reqmgrCouchDB = "reqmgr_workload_cache"

HOST = socket.gethostname().lower()
BASE_URL = "@@BASE_URL@@"
COUCH_URL = "%s/couchdb" % BASE_URL

REQMGR2 = "%s/reqmgr2" % BASE_URL
WEBURL = "%s/%s" % (COUCH_URL, workqueueDBName)
LOG_DB_URL = "%s/wmstats_logdb" % COUCH_URL
LOG_REPORTER = "global_workqueue"
AMQ_HOST_PORT = [('cms-mb.cern.ch', 61313)]

root = __file__.rsplit('/', 4)[0]
cache_dir = os.path.join(root, 'state', 'workqueue', 'cache')
os.environ['WMCORE_CACHE_DIR'] = cache_dir
os.environ['MAX_LUMIS_PER_WQE'] = '400000'

ROOTDIR = __file__.rsplit('/', 3)[0]
# load AMQ credentials
sys.path.append(os.path.join(ROOTDIR, 'auth/workqueue'))
try:
    from WorkQueueSecrets import USER_AMQ, PASS_AMQ, AMQ_TOPIC
except ImportError:
    print("Mocking WorkQueue credentials...")
    USER_AMQ=None
    PASS_AMQ=None
    AMQ_TOPIC=None

# Production service has to point to production Rucio, anything else will use pre-production
if BASE_URL == "https://cmsweb.cern.ch":
    RUCIO_AUTH_URL="https://cms-rucio-auth.cern.ch"
    RUCIO_URL="http://cms-rucio.cern.ch"
else:
    RUCIO_AUTH_URL="https://cms-rucio-auth-int.cern.ch"
    RUCIO_URL="http://cms-rucio-int.cern.ch"
RUCIO_ACCT = "wmcore_transferor"
RUCIO_RELVAL_ACCT = "wmcore_transferor_relval"

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
main.port = 8240
main.index = "ui"
# Defaults to allow any CMS authenticated user. Write APIs should require
# additional roles in SiteDB (i.e. "Admin" role for the "ReqMgr" group)
main.authz_defaults = {"role": None, "group": None, "site": None}
#set default logging (prevent duplicate)
main.log_screen = True

sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application) # string containing "globalworkqueue"
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS Workload Management Global WorkQueue"
app.title = " Global WorkQueue (GQ)"

views = config.section_("views")

def setWorkQueueCommonConfig(config):    
    # actual params needed to creating global queue
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
    config.queueParams['rucioAccount'] = RUCIO_ACCT
    config.queueParams['rucioAccountRelVal'] = RUCIO_RELVAL_ACCT
    config.queueParams['rucioAuthUrl'] = RUCIO_AUTH_URL
    config.queueParams['rucioUrl'] = RUCIO_URL

    config.reqMgrConfig = {}
    config.reqMgrConfig['reqmgr2_endpoint'] = REQMGR2
    config.reqMgrConfig['central_logdb_url'] = LOG_DB_URL
    config.reqMgrConfig['log_reporter'] = LOG_REPORTER

# Production instance of globalworkqueue, must be a production back-end
# Production vm vocms0740 and Testbed vm vocms0731 removed for k8s migration
if HOST.startswith("vocms0117"):
    extentions = config.section_("extensions")
    reqmgrInteraction = extentions.section_("reqmgrInteraction")
    reqmgrInteraction.object = "WMCore.GlobalWorkQueue.CherryPyThreads.ReqMgrInteractionTask.ReqMgrInteractionTask"
    setWorkQueueCommonConfig(reqmgrInteraction)
    reqmgrInteraction.interactDuration = 60 * 5 # every 5 minutes
    reqmgrInteraction.log_file = '%s/logs/workqueue/reqmgrInteractionTask-%s-%s.log' % (__file__.rsplit('/', 4)[0],HOST.split('.', 1)[0],time.strftime("%Y%m%d"))
    reqmgrInteraction.central_logdb_url = LOG_DB_URL
    reqmgrInteraction.log_reporter = LOG_REPORTER
    
    # location update
    locationUpdateTask = extentions.section_("locationUpdateTask")
    locationUpdateTask.object = "WMCore.GlobalWorkQueue.CherryPyThreads.LocationUpdateTask.LocationUpdateTask"
    setWorkQueueCommonConfig(locationUpdateTask)
    locationUpdateTask.locationUpdateDuration = 60 * 60 * 6 # every 6 hours
    locationUpdateTask.log_file = '%s/logs/workqueue/locationUpdateTask-%s-%s.log' % (__file__.rsplit('/', 4)[0],HOST.split('.', 1)[0],time.strftime("%Y%m%d"))
    locationUpdateTask.central_logdb_url = LOG_DB_URL
    locationUpdateTask.log_reporter = LOG_REPORTER
    
    # workqueue cleanup threads
    cleanUpTask = extentions.section_("cleanUpTask")
    cleanUpTask.object = "WMCore.GlobalWorkQueue.CherryPyThreads.CleanUpTask.CleanUpTask"
    setWorkQueueCommonConfig(cleanUpTask)
    cleanUpTask.cleanUpDuration = 60 * 10 # every 10 minutes
    cleanUpTask.log_file = '%s/logs/workqueue/cleanUpTask-%s-%s.log' % (__file__.rsplit('/', 4)[0],HOST.split('.', 1)[0],time.strftime("%Y%m%d"))
    cleanUpTask.central_logdb_url = LOG_DB_URL
    cleanUpTask.log_reporter = LOG_REPORTER
    
    # workqueue monitoring thread
    heartbeatMonitor = extentions.section_("heartbeatMonitor")
    heartbeatMonitor.object = "WMCore.GlobalWorkQueue.CherryPyThreads.HeartbeatMonitor.HeartbeatMonitor"
    setWorkQueueCommonConfig(heartbeatMonitor)
    heartbeatMonitor.heartbeatCheckDuration = 60 * 10 # every 10 minutes
    heartbeatMonitor.log_file = '%s/logs/workqueue/heartbeatMonitor-%s-%s.log' % (__file__.rsplit('/', 4)[0],HOST.split('.', 1)[0],time.strftime("%Y%m%d"))
    heartbeatMonitor.wmstats_url = "%s/%s" % (COUCH_URL, wmstatDBName)
    heartbeatMonitor.central_logdb_url = LOG_DB_URL
    heartbeatMonitor.log_reporter = LOG_REPORTER
    # AMQ MonIT settings
    # Commenting this logic for disabling prod workqueue on vocms0740 for k8s migration
    #if HOST.startswith("vocms0740"):
    #    heartbeatMonitor.post_to_amq = True
    #else:
    #    heartbeatMonitor.post_to_amq = False

    # Since testbed/prod workqueue VMs are disabled, this will always be False
    heartbeatMonitor.post_to_amq = False

    heartbeatMonitor.user_amq = USER_AMQ
    heartbeatMonitor.pass_amq = PASS_AMQ
    heartbeatMonitor.topic_amq = AMQ_TOPIC
    heartbeatMonitor.host_port_amq = AMQ_HOST_PORT
    #list all the thread need to be monitored
    heartbeatMonitor.thread_list = [a.object.split('.')[-1] for a in config.section_("extensions")]
