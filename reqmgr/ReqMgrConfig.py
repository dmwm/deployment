__all__ = []

import thread
import socket
import re
import os.path

import WMCore.HTTPFrontEnd.RequestManager.ReqMgrConfiguration as ReqMgrConfig
from WMCore.WMInit import getWMBASE

thread.stack_size(128*1024)
INSTALL = getWMBASE()

HOST = socket.getfqdn().lower()
COUCH = "https://%s/couchdb" % HOST

if re.match(r"^vocms0(?:13[689]|140|16[135]|30[67]|318)\.cern\.ch$", HOST):
  COUCH = "https://cmsweb.cern.ch/couchdb"
elif re.match(r"^vocms0(?:13[12])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-testbed.cern.ch/couchdb"
elif re.match(r"^vocms0127\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-dev.cern.ch/couchdb"
elif re.match(r"^vocms0126\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-sec.cern.ch/couchdb"

config = ReqMgrConfig.reqMgrConfig(installation=INSTALL, couchurl = COUCH)

TEMPLATES = os.path.normpath(os.path.join(INSTALL, '../../../data/templates/WMCore/WebTools'))
JAVASCRIPT_PATH = os.path.normpath(os.path.join(INSTALL, '../../../data/javascript'))
HTML_PATH = os.path.normpath(os.path.join(INSTALL, '../../../data/html'))

config.webapp_("reqmgr")
config.reqmgr.html = os.path.join(HTML_PATH, 'RequestManager')
config.reqmgr.templates = os.path.join(TEMPLATES, 'RequestManager')

config.reqmgr.views.active.reqMgr.html = os.path.join(HTML_PATH, 'RequestManager')
config.reqmgr.views.active.reqMgr.templates = TEMPLATES
config.reqmgr.views.active.rest.templates = TEMPLATES
config.reqmgr.security_roles.extend(['facops', 'FacOps'])

config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
#config.Webtools.environment = 'development'
config.Webtools.proxy_base = 'True'
config.Webtools.thread_pool = 30
config.Webtools.environment = 'production'