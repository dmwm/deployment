import socket
import re
import WMCore.HTTPFrontEnd.RequestManager.ReqMgrConfiguration as ReqMgrConfig
__all__ = []
from WMCore.WMInit import getWMBASE
import os.path
INSTALL = getWMBASE()

HOST = socket.getfqdn().lower()
COUCH = "https://%s/couchdb" % HOST
REQMGR_SVC = "https://%s/reqmgr/rest" % HOST

if re.match(r"^vocms(?:10[67]|13[689]|140)\.cern\.ch$", HOST):
  COUCH = "https://cmsweb.cern.ch/couchdb"
  REQMGR_SVC = "https://cmsweb.cern.ch/reqmgr/rest"
elif re.match(r"^vocms(?:13[23])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-testbed.cern.ch/couchdb"
  REQMGR_SVC = "https://cmsweb-testbed.cern.ch/reqmgr/rest"
elif re.match(r"^vocms127\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-dev.cern.ch/couchdb"
  REQMGR_SVC = "https://cmsweb-dev.cern.ch/reqmgr/rest"

config = ReqMgrConfig.reqMgrConfig(installation=INSTALL,
  couchurl = COUCH)

TEMPLATES = os.path.normpath(os.path.join(INSTALL, '../../templates/WMCore/WebTools'))
JAVASCRIPT_PATH = os.path.normpath(os.path.join(INSTALL, '../../javascript'))
HTML_PATH = os.path.normpath(os.path.join(INSTALL, '../../html'))

config.webapp_("reqmgr")
config.reqmgr.html = os.path.join(HTML_PATH, 'RequestManager')
config.reqmgr.templates = os.path.join(TEMPLATES, 'RequestManager')
config.reqmgr.views.active.GlobalMonitor.templates = os.path.join(TEMPLATES, 'GlobalMonitor')
config.reqmgr.views.active.GlobalMonitor.javascript = JAVASCRIPT_PATH
config.reqmgr.views.active.GlobalMonitor.html = HTML_PATH
config.reqmgr.views.active.reqMgr.html = os.path.join(HTML_PATH, 'RequestManager')
config.reqmgr.views.active.reqMgr.templates = TEMPLATES
config.reqmgr.views.active.rest.templates = TEMPLATES
config.reqmgr.views.active.monitorSvc.templates = TEMPLATES
config.reqmgr.views.active.monitorSvc.serviceURL = REQMGR_SVC
config.reqmgr.security_roles.extend(['facops', 'FacOps'])

config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
#config.Webtools.environment = 'development'
config.Webtools.proxy_base = 'True'
config.Webtools.environment = 'production'

