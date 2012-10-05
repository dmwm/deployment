import thread
thread.stack_size(128*1024)

import socket
import re
import WMCore.HTTPFrontEnd.RequestManager.ReqMgrConfiguration as ReqMgrConfig
__all__ = []
from WMCore.WMInit import getWMBASE
import os.path
INSTALL = getWMBASE()

HOST = socket.getfqdn().lower()
COUCH = "https://%s/couchdb" % HOST
ADD_MONITOR_FLAG = False

if re.match(r"^vocms(?:10[67]|13[689]|140|16[13])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb.cern.ch/couchdb"
elif re.match(r"^vocms(?:13[23])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-testbed.cern.ch/couchdb"
elif re.match(r"^vocms127\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-dev.cern.ch/couchdb"

config = ReqMgrConfig.reqMgrConfig(installation=INSTALL,
                                   couchurl=COUCH,
                                   addMonitor=ADD_MONITOR_FLAG,
                                   port=8245,
                                   reqMgrHost="http://%s:%d" % (socket.gethostname().lower(), 8245),
                                   configCouchDB='analysis_reqmgr_config_cache',
                                   workloadCouchDB='analysis_reqmgr_workload_cache',
                                   workloadSummaryCouchDB = "analysis_workloadsummary",
                                   wmstatCouchDB = "analysis_wmstats")

TEMPLATES = os.path.normpath(os.path.join(INSTALL, '../../../data/templates/WMCore/WebTools'))
JAVASCRIPT_PATH = os.path.normpath(os.path.join(INSTALL, '../../../data/javascript'))
HTML_PATH = os.path.normpath(os.path.join(INSTALL, '../../../data/html'))

config.webapp_("an_reqmgr")
config.an_reqmgr.html = os.path.join(HTML_PATH, 'RequestManager')
config.an_reqmgr.templates = os.path.join(TEMPLATES, 'RequestManager')

if ADD_MONITOR_FLAG:
    config.an_reqmgr.views.active.GlobalMonitor.templates = os.path.join(TEMPLATES, 'GlobalMonitor')
    config.an_reqmgr.views.active.GlobalMonitor.javascript = JAVASCRIPT_PATH
    config.an_reqmgr.views.active.GlobalMonitor.html = HTML_PATH
    config.an_reqmgr.views.active.monitorSvc.templates = TEMPLATES
    config.an_reqmgr.views.active.monitorSvc.serviceURL = "local"

config.an_reqmgr.views.active.assign.opshold = False
config.an_reqmgr.views.active.reqMgr.html = os.path.join(HTML_PATH, 'RequestManager')
config.an_reqmgr.views.active.reqMgr.templates = TEMPLATES
config.an_reqmgr.views.active.rest.templates = TEMPLATES
config.an_reqmgr.security_roles.extend(['facops', 'FacOps'])

config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
#config.Webtools.environment = 'development'
config.Webtools.proxy_base = 'True'
config.Webtools.thread_pool = 30
config.Webtools.environment = 'production'
