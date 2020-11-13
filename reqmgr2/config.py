"""
ReqMgr only configuration file.
Everything configurable in ReqMgr is defined here.
"""

import socket
import time
import sys
from WMCore.Configuration import Configuration
from os import path

HOST = socket.gethostname().lower()
BASE_URL = "@@BASE_URL@@"
DBS_INS = "@@DBS_INS@@"
COUCH_URL = "%s/couchdb" % BASE_URL
REQMGR2_URL = "%s/reqmgr2" % BASE_URL
LOG_DB_URL = "%s/wmstats_logdb" % COUCH_URL
LOG_REPORTER = "reqmgr2"
AMQ_HOST_PORT = [('cms-mb.cern.ch', 61313)]

ROOTDIR = __file__.rsplit('/', 3)[0]
# load AMQ credentials
sys.path.append(path.join(ROOTDIR, 'auth/reqmgr2'))
from ReqMgr2Secrets import USER_AMQ, PASS_AMQ, AMQ_TOPIC

config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
# The maximum number of requests which will be queued up before
# the server refuses to accept it (default -1, meaning no limit).
srv.accepted_queue_size = -1
srv.accepted_queue_timeout = 0
main.application = "reqmgr2"
main.port = 8246 # main application port it listens on
main.index = "ui"
# Defaults to allow any CMS authenticated user. Write APIs should require
# additional roles in SiteDB (i.e. "Admin" role for the "ReqMgr" group)
main.authz_defaults = {"role": None, "group": None, "site": None}
#set default logging (prevent duplicate)
main.log_screen = True

tools = main.section_("tools")
# provide CherryPy monitoring under: <hostname>/reqmgr2/data/stats
tools.section_("cpstats").on = False
tools.section_("cms_auth").key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application) # string containing "reqmgr2"
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS data operations Request Manager."
app.title = "CMS Request Manager (ReqMgr)"

views = config.section_("views")

# practical to have this kind of configuration values not in
# service related RPM (difficult/impossible to change in CMS web
# deployment) but in the deployment configuration for the service

# redirector for the REST API implemented handlers
data = views.section_("data")
data.object = "WMCore.ReqMgr.Service.RestApiHub.RestApiHub"
# The couch host is defined during deployment time.
data.couch_host = COUCH_URL
# main ReqMgr CouchDB database containing all requests with spec files attached
data.couch_reqmgr_db = "reqmgr_workload_cache"
# ReqMgr database containing groups, teams, software, etc
data.couch_reqmgr_aux_db = "reqmgr_auxiliary"
# ConfigCache - database with configuration documents
data.couch_config_cache_db = "reqmgr_config_cache"
data.couch_workload_summary_db = "workloadsummary"
data.couch_wmstats_db = "wmstats"
data.couch_wmdatamining_db = "wmdatamining"
data.couch_acdc_db = "acdcserver"
data.couch_workqueue_db = "workqueue"
data.central_logdb_url = LOG_DB_URL
data.log_reporter = LOG_REPORTER

# number of past days since when to display requests in the default view
data.default_view_requests_since_num_days = 30 # days
# resource to fetch CMS software versions and scramarch info from
data.tag_collector_url = "https://cmssdt.cern.ch/SDT/cgi-bin/ReleasesXML"
# another source at TC, returns directly JSON, but strangely formatted (e.g.
# keys are not present at easy item but defined in a dedicated item ...)
# https://cmssdt.cern.ch/tc/getReleasesInformation?release_state=Announced

# used for the StepChainParentageFixTask; use dbs testbed for private vm test
if DBS_INS == "private_vm":
    data.dbs_url = "https://cmsweb-testbed.cern.ch/dbs/int/global/DBSWriter"
else:
    data.dbs_url = "%s/dbs/%s/global/DBSWriter" % (BASE_URL, DBS_INS)

# web user interface
ui = views.section_("ui")
ui.static_content_dir = path.join(path.abspath(ROOTDIR),
                                 "apps",
                                 main.application,
                                 "data")
#ui.object = "WMCore.ReqMgr.WebGui.FrontPage.FrontPage"
ui.object = "WMCore.ReqMgr.Web.ReqMgrService.ReqMgrService"
ui.tmpldir = path.join(ui.static_content_dir, "html", "ReqMgr", "templates")
ui.imgdir = path.join(ui.static_content_dir, "html", "ReqMgr", "img")
ui.cssdir = path.join(ui.static_content_dir, "html", "ReqMgr", "style")
ui.jsdir = path.join(ui.static_content_dir, "html", "ReqMgr", "javascript")
#TODO : need to find correct location for this
ui.sdir = path.join(ui.static_content_dir, "html", "ReqMgr", "javascript")

ui.yuidir = path.join(ui.static_content_dir, "html", "ReqMgr", "yui")
ui.admin = 'cms-service-webtools@cern.ch'
ui.title = 'CMS ReqMgr Documentation'
ui.description = 'Documentation on the ReqMgrService'
ui.base = '/reqmgr2'
ui.index = 'reqmgr2' # this part must be activated, see below
ui.reqmgr = data # this part contains uiuration for ReqMgr REST API, see above
# This need to be removed when ReqMgr Client is removed
ui.reqmgr.reqmgr2_url = REQMGR2_URL # this part contains uiuration for ReqMgr REST API, see above
ui.reqmgr.wmstats_url = "%s/wmstatsserver" % BASE_URL
ui_main = ui.section_("main")
ui_main.application = ui.index
#ui_main.authz_defaults = {"role": None, "group": None, "site": None, "policy": "dangerously_insecure"}

extentions = config.section_("extensions")
# Production instance of wmdatamining, must be a production back-end
if HOST.startswith("vocms0766") or HOST.startswith("vocms0731") or HOST.startswith("vocms0117"):
#     wmdatamining = extentions.section_("wmdatamining")
#     wmdatamining.object = "WMCore.ReqMgr.CherryPyThreads.WMDataMining.WMDataMining"
#     wmdatamining.wmstats_url = "%s/%s" % (data.couch_host, data.couch_wmstats_db)
#     wmdatamining.reqmgrdb_url = "%s/%s" % (data.couch_host, data.couch_reqmgr_db)
#     wmdatamining.wmdatamining_url = "%s/%s" % (data.couch_host, data.couch_wmdatamining_db)
#     wmdatamining.mcm_url = "https://cms-pdmv.cern.ch/mcm"
#     wmdatamining.mcm_cert = "%s/auth/reqmgr2/dmwm-service-cert.pem" % ROOTDIR
#     wmdatamining.mcm_key = "%s/auth/reqmgr2/dmwm-service-key.pem" % ROOTDIR
#     wmdatamining.mcm_tmp_dir = "%s/state/reqmgr2/tmp" % __file__.rsplit('/', 4)[0]
#     wmdatamining.activeDuration = 60 * 15  # every 15 min
#     wmdatamining.archiveDuration = 60 * 60 * 4 # every 4 hours
#     wmdatamining.log_file = '%s/logs/reqmgr2/wmdataminig-%s.log' % (__file__.rsplit('/', 4)[0], time.strftime("%Y%m%d"))
#     wmdatamining.central_logdb_url = LOG_DB_URL
#     wmdatamining.log_reporter = LOG_REPORTER
    
    # ACDC/workqueue cleanup threads
    couchCleanup = extentions.section_("couchCleanup")
    couchCleanup.object = "WMCore.ReqMgr.CherryPyThreads.CouchDBCleanup.CouchDBCleanup"
    couchCleanup.reqmgr2_url = REQMGR2_URL
    couchCleanup.reqmgrdb_url = "%s/%s" % (data.couch_host, data.couch_reqmgr_db)
    couchCleanup.acdc_url = "%s/%s" % (data.couch_host, data.couch_acdc_db)
    couchCleanup.acdcCleanDuration = 60 * 60 * 4 # every 4 hours
    couchCleanup.auxCleanDuration = 60 * 60 * 12 # every 12 hours
    couchCleanup.workqueue_url = "%s/%s" % (data.couch_host, data.couch_workqueue_db)
    couchCleanup.workqueueCleanDuration = 60 * 60 * 12 # every 12 hours
    couchCleanup.log_file = '%s/logs/reqmgr2/couchCleanup-%s-%s.log' % (__file__.rsplit('/', 4)[0], HOST.split('.', 1)[0], time.strftime("%Y%m%d"))
    couchCleanup.central_logdb_url = LOG_DB_URL
    couchCleanup.log_reporter = LOG_REPORTER

    # status change task
    parentageFixTask = extentions.section_("parentageFixTask")
    parentageFixTask.object = "WMCore.ReqMgr.CherryPyThreads.StepChainParentageFixTask.StepChainParentageFixTask"
    parentageFixTask.dbs_url = data.dbs_url
    parentageFixTask.reqmgrdb_url = "%s/%s" % (data.couch_host, data.couch_reqmgr_db)
    parentageFixTask.parentageFixDuration = 60 * 180  # every 3 hours
    parentageFixTask.log_file = '%s/logs/reqmgr2/parentageFixTask-%s-%s.log' % (__file__.rsplit('/', 4)[0], HOST.split('.', 1)[0], time.strftime("%Y%m%d"))
    parentageFixTask.central_logdb_url = LOG_DB_URL
    parentageFixTask.log_reporter = LOG_REPORTER

if HOST.startswith("vocms0766") or HOST.startswith("vocms0731") or HOST.startswith("vocms0117"):
    # status change task 
    statusChangeTasks = extentions.section_("statusChangeTasks")
    statusChangeTasks.object = "WMCore.ReqMgr.CherryPyThreads.StatusChangeTasks.StatusChangeTasks"
    statusChangeTasks.reqmgr2_url = REQMGR2_URL
    statusChangeTasks.wmstats_url = "%s/wmstatsserver" % BASE_URL
    statusChangeTasks.workqueue_url = "%s/%s" % (data.couch_host, data.couch_workqueue_db)
    statusChangeTasks.archiveDelayHours = 24 * 3 # archive workflows after being for 3 days in the previous status
    statusChangeTasks.checkStatusDuration = 60 * 10  # every 10 min
    statusChangeTasks.enableMSStatusTransition = False
    statusChangeTasks.log_file = '%s/logs/reqmgr2/statusChangeTasks-%s-%s.log' % (__file__.rsplit('/', 4)[0], HOST.split('.', 1)[0], time.strftime("%Y%m%d"))
    statusChangeTasks.central_logdb_url = LOG_DB_URL
    statusChangeTasks.log_reporter = LOG_REPORTER

    # AuxCache update threads
    auxCacheUpdateTasks = extentions.section_("auxCacheUpdateTasks")
    auxCacheUpdateTasks.object = "WMCore.ReqMgr.CherryPyThreads.AuxCacheUpdateTasks.AuxCacheUpdateTasks"
    auxCacheUpdateTasks.reqmgr2_url = REQMGR2_URL
    auxCacheUpdateTasks.tagCollectDuration = 60 * 60  # every 1 hour
    auxCacheUpdateTasks.tagcollect_url = "https://cmssdt.cern.ch/SDT/cgi-bin/ReleasesXML"
    auxCacheUpdateTasks.tagcollect_args = {"anytype": 1, "anyarch": 1}
    auxCacheUpdateTasks.unified_url = "https://raw.githubusercontent.com/CMSCompOps/WmAgentScripts/master/unifiedConfiguration.json"
    auxCacheUpdateTasks.log_file = '%s/logs/reqmgr2/auxCacheUpdateTasks-%s-%s.log' % (__file__.rsplit('/', 4)[0], HOST.split('.', 1)[0], time.strftime("%Y%m%d"))
    auxCacheUpdateTasks.central_logdb_url = LOG_DB_URL
    auxCacheUpdateTasks.log_reporter = LOG_REPORTER

    # construct list of locked parent datasets
    parentTask = extentions.section_("parentLock")
    parentTask.object = "WMCore.ReqMgr.CherryPyThreads.BuildParentLock.BuildParentLock"
    parentTask.dbs_url = data.dbs_url
    parentTask.reqmgrdb_url = "%s/%s" % (data.couch_host, data.couch_reqmgr_db)
    parentTask.reqmgr2_url = "%s/reqmgr2" % BASE_URL
    parentTask.central_logdb_url = LOG_DB_URL
    parentTask.log_reporter = LOG_REPORTER
    parentTask.updateParentsInterval = 60 * 10  # every 10 minutes
    parentTask.log_file = '%s/logs/reqmgr2/parentTask-%s-%s.log' % (
    __file__.rsplit('/', 4)[0], HOST.split('.', 1)[0], time.strftime("%Y%m%d"))

    # heartbeat monitor task
    heartbeatMonitor = extentions.section_("heartbeatMonitor")
    heartbeatMonitor.object = "WMCore.ReqMgr.CherryPyThreads.HeartbeatMonitor.HeartbeatMonitor"
    heartbeatMonitor.wmstats_url = "%s/%s" % (data.couch_host, data.couch_wmstats_db)
    heartbeatMonitor.wmstatsSvc_url = "%s/wmstatsserver" % BASE_URL
    heartbeatMonitor.heartbeatCheckDuration = 60 * 10  # every 10 min
    heartbeatMonitor.log_file = '%s/logs/reqmgr2/heartbeatMonitor-%s-%s.log' % (__file__.rsplit('/', 4)[0], HOST.split('.', 1)[0], time.strftime("%Y%m%d"))
    heartbeatMonitor.central_logdb_url = LOG_DB_URL
    heartbeatMonitor.log_reporter = LOG_REPORTER
    # AMQ MonIT settings
    if HOST.startswith("vocms0766") or HOST.startswith("vocms0731"):
        heartbeatMonitor.post_to_amq = True
    else:
        heartbeatMonitor.post_to_amq = False
    heartbeatMonitor.user_amq = USER_AMQ
    heartbeatMonitor.pass_amq = PASS_AMQ
    heartbeatMonitor.topic_amq = AMQ_TOPIC
    heartbeatMonitor.host_port_amq = AMQ_HOST_PORT
    #list all the thread need to be monitored
    heartbeatMonitor.thread_list = [a.object.split('.')[-1] for a in config.section_("extensions")]
