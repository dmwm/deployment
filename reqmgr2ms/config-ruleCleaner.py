"""
MicroService RuleCleaner configuration file.
"""

import socket
import sys
import time
from os import path

from WMCore.Configuration import Configuration

# globals
HOST = socket.gethostname().lower()
BASE_URL = "@@BASE_URL@@"
DBS_INS = "@@DBS_INS@@"
COUCH_URL = "%s/couchdb" % BASE_URL
LOG_DB_URL = "%s/wmstats_logdb" % COUCH_URL
LOG_REPORTER = "reqmgr2ms_ruleCleaner"
ROOTDIR = __file__.rsplit('/', 3)[0]
AMQ_HOST_PORT = [('cms-mb.cern.ch', 61313)]

# load AMQ credentials
sys.path.append(path.join(ROOTDIR, 'auth/reqmgr2ms'))
from ReqMgr2MSSecrets import USER_AMQ, PASS_AMQ, AMQ_TOPIC

if BASE_URL == "https://cmsweb.cern.ch":
    RUCIO_AUTH_URL = "https://cms-rucio-auth.cern.ch"
    RUCIO_URL = "http://cms-rucio.cern.ch"
    RUCIO_WMA_ACCT = "wma_prod"
    ARCH_DELAY_HOURS = 24 * 2
else:
    RUCIO_AUTH_URL = "https://cms-rucio-auth-int.cern.ch"
    RUCIO_URL = "http://cms-rucio-int.cern.ch"
    RUCIO_WMA_ACCT = "wma_test"
    ARCH_DELAY_HOURS = 6
RUCIO_MSTR_ACCT = "wmcore_transferor"
RUCIO_MSTR_RELVAL_ACCT = "wmcore_transferor_relval"

config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "ms-rulecleaner"
main.port = 8244  # main application port it listens on
main.index = 'ui'  # Configuration requires index attribute

# Security configuration
main.authz_defaults = {"role": None, "group": None, "site": None}
# set default logging (prevent duplicate)
main.log_screen = True

sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application)
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS Workload Management MicroServices"
app.title = "CMS MicroService RuleCleaner"

# define different views for our application
views = config.section_("views")
# web UI interface
ui = views.section_('ui')
ui.object = 'WMCore.MicroService.WebGui.FrontPage.FrontPage'
ui.static = ROOTDIR

# REST interface
data = views.section_('data')
data.object = 'WMCore.MicroService.Service.RestApiHub.RestApiHub'
# The couch host is defined during deployment time.
data.couch_host = COUCH_URL
data.couch_wmstats_db = "wmstats"
data.manager = 'WMCore.MicroService.MSCore.MSManager.MSManager'
data.reqmgr2Url = "%s/reqmgr2" % BASE_URL
data.msOutputUrl = "%s/ms-output" % BASE_URL
data.wmstatsUrl = "%s/wmstatsserver" % BASE_URL
data.logDBUrl = "%s/couchdb/wmstats_logdb" % BASE_URL
data.logDBReporter = 'reqmgr2ms_ruleCleaner'
data.archiveDelayHours = ARCH_DELAY_HOURS
data.limitRequestsPerCycle = 500
data.verbose = True
data.interval = 60 * 60 * 8  # run it every 8 hours
data.services = ['ruleCleaner']
data.rucioAccount = RUCIO_WMA_ACCT
data.rucioWmaAccount = RUCIO_WMA_ACCT
data.rucioMstrAccount = RUCIO_MSTR_ACCT
data.rucioMstrRelValAccount = RUCIO_MSTR_RELVAL_ACCT
data.rucioAuthUrl = RUCIO_AUTH_URL
data.rucioUrl = RUCIO_URL
data.enableRealMode = True
if DBS_INS == "private_vm":
    data.dbsUrl = "https://cmsweb-testbed.cern.ch/dbs/int/global/DBSReader"
else:
    data.dbsUrl = "%s/dbs/%s/global/DBSReader" % (BASE_URL, DBS_INS)

# heartbeat monitor task
extentions = config.section_("extensions")
heartbeatMonitor = extentions.section_("heartbeatMonitor")
heartbeatMonitor.object = "WMCore.MicroService.CherryPyThreads.HeartbeatMonitor.HeartbeatMonitor"
heartbeatMonitor.wmstats_url = "%s/%s" % (data.couch_host, data.couch_wmstats_db)
heartbeatMonitor.wmstatsSvc_url = "%s/wmstatsserver" % BASE_URL
heartbeatMonitor.heartbeatCheckDuration = 60 * 10  # every 10 min
heartbeatMonitor.log_file = '%s/logs/reqmgr2ms/heartbeatMonitor_rulecleaner-%s-%s.log' % (__file__.rsplit('/', 4)[0],
                                                                                          HOST.split('.', 1)[0],
                                                                                          time.strftime("%Y%m%d"))
heartbeatMonitor.central_logdb_url = LOG_DB_URL
heartbeatMonitor.log_reporter = LOG_REPORTER
# AMQ MonIT settings
heartbeatMonitor.post_to_amq = False
heartbeatMonitor.user_amq = USER_AMQ
heartbeatMonitor.pass_amq = PASS_AMQ
heartbeatMonitor.topic_amq = AMQ_TOPIC
heartbeatMonitor.host_port_amq = AMQ_HOST_PORT
# list all the thread need to be monitored
heartbeatMonitor.thread_list = [a.object.split('.')[-1] for a in config.section_("extensions")]
