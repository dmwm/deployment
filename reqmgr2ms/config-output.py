"""
MicroService Output configuration file.
"""

import socket
import time
import sys
from os import path
from WMCore.Configuration import Configuration

# globals
HOST = socket.gethostname().lower()
BASE_URL = "@@BASE_URL@@"
DBS_INS = "@@DBS_INS@@"
COUCH_URL = "%s/couchdb" % BASE_URL
LOG_DB_URL = "%s/wmstats_logdb" % COUCH_URL
LOG_REPORTER = "reqmgr2ms_output"
ROOTDIR = __file__.rsplit('/', 3)[0]
AMQ_HOST_PORT = [('cms-mb.cern.ch', 61313)]

# load AMQ credentials
sys.path.append(path.join(ROOTDIR, 'auth/reqmgr2ms'))
from ReqMgr2MSSecrets import USER_AMQ, PASS_AMQ, AMQ_TOPIC

RUCIO_ACCT = "wmcore_output"
RULE_LIFETIME = 30 * 24 * 60 * 60  # 30 days
RULE_LIFETIME_RELVAL = 12 * 30 * 24 * 60 * 60  # 12 months
if BASE_URL == "https://cmsweb.cern.ch":
    RUCIO_AUTH_URL="https://cms-rucio-auth.cern.ch"
    RUCIO_URL="http://cms-rucio.cern.ch"
    SEND_NOTIFICATION=True
    ENABLE_DATA_PLACEMENT=True
else:
    RUCIO_AUTH_URL="https://cms-rucio-auth-int.cern.ch"
    RUCIO_URL="http://cms-rucio-int.cern.ch"
    SEND_NOTIFICATION=False
    ENABLE_DATA_PLACEMENT=False

config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "ms-output"
main.port = 8245  # main application port it listens on
main.index = 'ui' # Configuration requires index attribute

# Security configuration
main.authz_defaults = {"role": None, "group": None, "site": None}
#set default logging (prevent duplicate)
main.log_screen = True

sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application)
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS Workload Management MicroServices"
app.title = "CMS MicroService Output"

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
data.limitRequestsPerCycle = 500
# Allows or not some alert notifications to be sent to the production-admin egroup
data.sendNotification = SEND_NOTIFICATION
data.verbose = True
data.interval = 60 * 60 * 1  # run it every hour
data.services = ['output']
data.enableDataPlacement = ENABLE_DATA_PLACEMENT
data.enableRelValCustodial = False
data.excludeDataTier = []
# RelVal output data placement policy, note that "default" corresponds
# to the destination in case the datatier name is not defined in the policy
# Note: when multiple destinations are provided, each one gets a copy of the data.
data.relvalPolicy = [{"datatier": "GEN-SIM", "destinations": ["T2_CH_CERN"]},
                     {"datatier": "ALCARECO", "destinations": ["T2_CH_CERN"]},
                     {"datatier": "default", "destinations": ["T2_CH_CERN"]}]
data.rucioRSEAttribute = None  # "ddm_quota"
data.rucioDiskRuleWeight = "ddm_quota"
data.rucioTapeExpression = "rse_type=TAPE\cms_type=test"  # "rse_type=TAPE\cms_type=test\\rse=T0_CH_CERN_Tape"
data.rulesLifetime = RULE_LIFETIME
data.ruleLifetimeRelVal = RULE_LIFETIME_RELVAL
data.rucioAccount = RUCIO_ACCT
data.rucioAuthUrl = RUCIO_AUTH_URL
data.rucioUrl = RUCIO_URL
# if private_vm, just fallback to preprod DBS
if DBS_INS == "private_vm":
    data.dbsUrl = "https://cmsweb-testbed.cern.ch/dbs/int/global/DBSReader"
else:
    data.dbsUrl = "%s/dbs/%s/global/DBSReader" % (BASE_URL, DBS_INS)
    data.dbsUrl = data.dbsUrl.replace("cmsweb.cern.ch", "cmsweb-prod.cern.ch")

# heartbeat monitor task
extentions = config.section_("extensions")
heartbeatMonitor = extentions.section_("heartbeatMonitor")
heartbeatMonitor.object = "WMCore.MicroService.CherryPyThreads.HeartbeatMonitor.HeartbeatMonitor"
heartbeatMonitor.wmstats_url = "%s/%s" % (data.couch_host, data.couch_wmstats_db)
heartbeatMonitor.wmstatsSvc_url = "%s/wmstatsserver" % BASE_URL
heartbeatMonitor.heartbeatCheckDuration = 60 * 10  # every 10 min
heartbeatMonitor.log_file = '%s/logs/reqmgr2ms/heartbeatMonitor_output-%s-%s.log' % (__file__.rsplit('/', 4)[0], HOST.split('.', 1)[0], time.strftime("%Y%m%d"))
heartbeatMonitor.central_logdb_url = LOG_DB_URL
heartbeatMonitor.log_reporter = LOG_REPORTER
# AMQ MonIT settings
heartbeatMonitor.post_to_amq = False
heartbeatMonitor.user_amq = USER_AMQ
heartbeatMonitor.pass_amq = PASS_AMQ
heartbeatMonitor.topic_amq = AMQ_TOPIC
heartbeatMonitor.host_port_amq = AMQ_HOST_PORT
#list all the thread need to be monitored
heartbeatMonitor.thread_list = [a.object.split('.')[-1] for a in config.section_("extensions")]
