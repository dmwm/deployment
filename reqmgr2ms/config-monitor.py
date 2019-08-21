"""
MicroService Monitor configuration file.
"""

import socket
from WMCore.Configuration import Configuration

# globals
HOST = socket.gethostname().lower()
BASE_URL = "@@BASE_URL@@"
DBS_INS = "@@DBS_INS@@"
LOG_REPORTER = "reqmgr2ms"
ROOTDIR = __file__.rsplit('/', 3)[0]

if BASE_URL == "https://cmsweb.cern.ch":
    RUCIO_ACCT = "production"
else:
    RUCIO_ACCT="wmagent_testing"

config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "ms-monitor"
main.port = 8248  # main application port it listens on
main.index = 'data' # Configuration requires index attribute

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
app.title = "CMS MicroService Monitor"

# define different views for our application
views = config.section_("views")
# web UI interface
ui = views.section_('web') # was section 'ui'
ui.object = 'WMCore.MicroService.WebGui.FrontPage.FrontPage'
ui.static = ROOTDIR

# REST interface
data = views.section_('data')
data.object = 'WMCore.MicroService.Service.RestApiHub.RestApiHub'
data.manager = 'WMCore.MicroService.Unified.MSManager.MSManager'
data.reqmgr2Url = "%s/reqmgr2" % BASE_URL
data.readOnly = True
data.verbose = True
data.interval = 600
data.services = ['monitor']
data.rucioAccount = RUCIO_ACCT
data.phedexUrl = "https://cmsweb.cern.ch/phedex/datasvc/json/prod"
# if private_vm, just fallback to preprod DBS
if DBS_INS == "private_vm":
    data.dbsUrl = "https://cmsweb-testbed.cern.ch/dbs/int/global/DBSReader"
else:
    data.dbsUrl = "%s/dbs/%s/global/DBSReader" % (BASE_URL, DBS_INS)
