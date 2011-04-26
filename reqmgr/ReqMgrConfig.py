import WMCore.HTTPFrontEnd.RequestManager.ReqMgrConfiguration as ReqMgrConfig
__all__ = []
from WMCore.WMInit import getWMBASE
import os.path
INSTALL = getWMBASE()

config = ReqMgrConfig.reqMgrConfig(installation=INSTALL,
  couchurl = 'http://localhost:5984')

config.webapp_("reqmgr")
config.reqmgr.templates = os.path.join(INSTALL, '../../templates/WMCore/WebTools/RequestManager')
TEMPLATES= os.path.join(INSTALL, '../../templates/WMCore/WebTools')
config.reqmgr.views.active.RequestOverview.templates = TEMPLATES
config.reqmgr.views.active.RequestOverview.javascript = os.path.join(INSTALL, '../../javascript')
config.reqmgr.views.active.RequestOverview.html  = os.path.join(INSTALL, '../../html')
config.reqmgr.views.active.reqMgr.templates = TEMPLATES

config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
#config.Webtools.environment = 'development'
config.Webtools.proxy_base = 'True'
config.Webtools.environment = 'production'

