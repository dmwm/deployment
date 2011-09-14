import socket
import re
import WMCore.HTTPFrontEnd.RequestManager.ReqMgrConfiguration as ReqMgrConfig
__all__ = []
from WMCore.WMInit import getWMBASE
import os.path
INSTALL = getWMBASE()

HOST = socket.getfqdn().lower()
COUCH = "https://%s/couchdb" % HOST

if re.match(r"^vocms(?:10[67]|13[689]|140)\.cern\.ch$", HOST):
  COUCH = "https://cmsweb.cern.ch/couchdb"
elif re.match(r"^vocms(?:13[23])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-testbed.cern.ch/couchdb"
elif re.match(r"^vocms127\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-dev.cern.ch/couchdb"

config = ReqMgrConfig.reqMgrConfig(installation=INSTALL,
  couchurl = COUCH)

config.webapp_("reqmgr")

config.reqmgr.templates = os.path.normpath(os.path.join(INSTALL, '../../templates/WMCore/WebTools/RequestManager'))
WEBTOOLSTEMPLATES= os.path.normpath(os.path.join(INSTALL, '../../templates/WMCore/WebTools'))
HTML=os.path.normpath(os.path.join(INSTALL, '../../html/RequestManager'))
config.reqmgr.html = HTML
config.reqmgr.views.active.reqMgr.templates = WEBTOOLSTEMPLATES
config.reqmgr.views.active.rest.templates = WEBTOOLSTEMPLATES
config.reqmgr.views.active.reqMgr.html = os.path.join(INSTALL, '../../html/RequestManager')
config.reqmgr.security_roles.extend(['facops', 'FacOps'])

config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
#config.Webtools.environment = 'development'
config.Webtools.proxy_base = 'True'
config.Webtools.environment = 'production'

