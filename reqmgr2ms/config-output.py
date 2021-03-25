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
    RUCIO_AUTH_URL="https://cmsrucio-auth-int.cern.ch"
    RUCIO_URL="http://cmsrucio-int.cern.ch"
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
data.manager = 'WMCore.MicroService.MSManager.MSManager'
data.reqmgr2Url = "%s/reqmgr2" % BASE_URL
data.limitRequestsPerCycle = 500
# Allows or not some alert notifications to be sent to the production-admin egroup
data.sendNotification = SEND_NOTIFICATION
data.verbose = True
data.interval = 60 * 60 * 1  # run it every hour
data.services = ['output']
# This tape pledges was extracted from WLCG Rebus and will be needed for the PhEDEx-based data placement
# https://wlcg-rebus.cern.ch/core/pledge/list/?vo_name=CMS&year=2020&type=Tape
# Note that a few sites are storing HI data as well, so we need to subtract the storage
# usage for those sites by the amount of Heavy Ion data (or increase the quota here ;))
# Numbers are: FNAL 15.3 PB, IN2P3: 3.0 PB, JINR: 1.1 PB
# Note that these values are in TeraBytes (TB) and will only be used ih the PhEDEx era
data.tapePledges = {"T0_CH_CERN_MSS": 99000,
                    "T1_US_FNAL_MSS": 88000 + 15300,
                    "T1_IT_CNAF_MSS": 28600,
                    "T1_DE_KIT_MSS": 22000,
                    "T1_FR_CCIN2P3_MSS": 18700 + 3000,
                    "T1_UK_RAL_MSS": 17600,
                    "T1_RU_JINR_MSS": 10000 + 1100,
                    "T1_ES_PIC_MSS": 8800}
data.enableDataPlacement = ENABLE_DATA_PLACEMENT
data.enableRelValCustodial = False
data.excludeDataTier = []
data.rucioRSEAttribute = "ddm_quota"
data.rucioDiskRuleWeight = "ddm_quota"
data.rucioTapeExpression = "rse_type=TAPE\cms_type=test"  # "rse_type=TAPE\cms_type=test\\rse=T0_CH_CERN_Tape"
data.rulesLifetime = RULE_LIFETIME
data.ruleLifetimeRelVal = RULE_LIFETIME_RELVAL
data.rucioAccount = RUCIO_ACCT
data.rucioAuthUrl = RUCIO_AUTH_URL
data.rucioUrl = RUCIO_URL

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
