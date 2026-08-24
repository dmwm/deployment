"""
MicroService Transferor configuration file.
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
LOG_REPORTER = "reqmgr2ms_transferor"
ROOTDIR = __file__.rsplit('/', 3)[0]
AMQ_HOST_PORT = [('cms-mb.cern.ch', 61313)]
RUCIO_AUTH_URL="https://cms-rucio-auth.cern.ch"
RUCIO_URL="http://cms-rucio.cern.ch"
RULE_LIFETIME=3 * 24 * 60 * 60  # 3 days

# load AMQ credentials
sys.path.append(path.join(ROOTDIR, 'auth/reqmgr2ms'))
from ReqMgr2MSSecrets import USER_AMQ, PASS_AMQ, AMQ_TOPIC

config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "ms-transferor"
main.port = 8247  # main application port it listens on
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
app.title = "CMS MicroService Transferor"

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
data.enableStatusTransition = True
data.enableDataTransfer = True
data.verbose = True
data.interval = 600
data.services = ['transferor']
data.quotaUsage = 0.9
data.minimumThreshold = 1 * (1000 ** 4)  # 1 TB (terabyte)
data.rulesLifetime = RULE_LIFETIME
data.rucioRuleWeight = "ddm_quota"
data.rucioAccount = "wmcore_transferor"
data.rucioAuthUrl = RUCIO_AUTH_URL
data.rucioUrl = RUCIO_URL
data.toAddr = ["alan.malta@cern.ch", "todor.trendafilov.ivanov@cern.ch", "kenyi.paolo.hurtado.anampa@cern.ch", "h.ozturk@cern.ch"]
data.warningTransferThreshold = 100. * (1000 ** 4) # 100 TB (terabyte)
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
heartbeatMonitor.log_file = '%s/logs/reqmgr2ms/heartbeatMonitor_transferor-%s-%s.log' % (__file__.rsplit('/', 4)[0], HOST.split('.', 1)[0], time.strftime("%Y%m%d"))
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
