"""
ReqMgr only configuration file.
Everything configurable in ReqMgr is defined here.

"""

import socket
import time
from WMCore.Configuration import Configuration
from os import path

HOST = socket.gethostname().lower()
BASE_URL = "@@BASE_URL@@"
DBS_INS = "@@DBS_INS@@"
COUCH_URL = "%s/couchdb" % BASE_URL
LOG_DB_URL = "%s/wmstats_logdb" % COUCH_URL

ROOTDIR = __file__.rsplit('/', 3)[0]
config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "wmstatsserver"
main.application_dir = "reqmon"
main.port = 8249 # main application port it listens on
main.index = "ui"
# Defaults to allow any CMS authenticated user. Write APIs should require
# additional roles in SiteDB (i.e. "Admin" role for the "ReqMgr" group)
main.authz_defaults = {"role": None, "group": None, "site": None}

sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application) # string containing "wmstats"
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS data operations Request Manager."
app.title = "CMS WMStats (ReqMon)"

views = config.section_("views")

# practical to have this kind of configuration values not in
# service related RPM (difficult/impossible to change in CMS web
# deployment) but in the deployment configuration for the service

# redirector for the REST API implemented handlers
data = views.section_("data")
data.object = "WMCore.WMStats.Service.RestApiHub.RestApiHub"
# The couch host is defined during deployment time.
data.couch_host = COUCH_URL
# main ReqMgr CouchDB database containing all requests with spec files attached
data.couch_reqmgr_db = "reqmgr_workload_cache"
# ReqMgr database containing groups, teams, software, etc
data.couch_config_cache_db = "reqmgr_config_cache"
data.couch_workload_summary_db = "workloadsummary"
data.couch_wmstats_db = "wmstats"
data.central_logdb_url = LOG_DB_URL
data.log_reporter = "wmstats"

if DBS_INS == "private_vm":
    data.dbs_url = "https://cmsweb-testbed.cern.ch/dbs/int/global/DBSReader"
else:
    data.dbs_url = "%s/dbs/%s/global/DBSReader" % (BASE_URL, DBS_INS)

# web user interface
ui = views.section_("ui")
ui.object = "WMCore.WMStats.WebGui.FrontPage.FrontPage"
ui.static_content_dir = path.join(path.abspath(ROOTDIR),
                                 "apps",
                                 main.application_dir,
                                 "data")

extentions = config.section_("extensions")

# wmstats data cache update (This need to be updated for all backend since this is memory cache)
dataCacheTasks = extentions.section_("dataCacheTasks")
dataCacheTasks.object = "WMCore.WMStats.CherryPyThreads.DataCacheUpdate.DataCacheUpdate"
dataCacheTasks.wmstats_url = "%s/%s" % (data.couch_host, data.couch_wmstats_db)
dataCacheTasks.reqmgrdb_url = "%s/%s" % (data.couch_host, data.couch_reqmgr_db)
dataCacheTasks.dataCacheUpdateDuration = 60 * 5 # every 5 min
dataCacheTasks.log_file = '%s/logs/reqmon/dataCacheTasks-%s.log' % (__file__.rsplit('/', 4)[0], time.strftime("%Y%m%d"))

# Production/testbed instance of logdb, must be a production/testbed back-end
if  HOST.startswith("vocms0307") or HOST.startswith("vocms0131"):
    
    # LogDB task (update and clean up)
    logDBTasks = extentions.section_("logDBTasks")
    logDBTasks.object = "WMCore.WMStats.CherryPyThreads.LogDBTasks.LogDBTasks"
    logDBTasks.central_logdb_url = data.central_logdb_url
    logDBTasks.log_reporter = data.log_reporter
    logDBTasks.logDBCleanDuration = 60 * 60 * 24 * 1 # 1 day
    logDBTasks.logDBUpdateDuration = 60 * 10 # every 10 min
    logDBTasks.log_file = '%s/logs/reqmon/logDBTasks-%s.log' % (__file__.rsplit('/', 4)[0], time.strftime("%Y%m%d"))
    
    # Cleaning up wmstats db
    cleanUpTask = extentions.section_("cleanUpTask")
    cleanUpTask.object = "WMCore.WMStats.CherryPyThreads.CleanUpTask.CleanUpTask"
    cleanUpTask.wmstats_url = "%s/%s" % (data.couch_host, data.couch_wmstats_db)
    cleanUpTask.reqmgrdb_url = "%s/%s" % (data.couch_host, data.couch_reqmgr_db)
    cleanUpTask.reqdb_couch_app = "ReqMgr"
    cleanUpTask.central_logdb_url = data.central_logdb_url
    cleanUpTask.log_reporter = data.log_reporter
    cleanUpTask.DataKeepDays = 0.125 # 3 hours - unit is day
    cleanUpTask.archivedCleanUpDuration = 60 * 60 * 12  # every 12 hours
    cleanUpTask.log_file = '%s/logs/reqmon/cleanUpTask-%s.log' % (__file__.rsplit('/', 4)[0], time.strftime("%Y%m%d"))
