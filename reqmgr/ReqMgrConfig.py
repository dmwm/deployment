import os, re, socket
from WMCore.WMInit import getWMBASE
from WMCore.Configuration import Configuration
from ReqMgrSecrets import connectUrl
__all__ = []

BASEDIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

PORT = 8240
HOST = socket.gethostname().lower()
COUCH = "http://localhost:5984"
TEMPLATES = os.path.join(getWMBASE(), 'templates/WMCore/WebTools/RequestManager')
YUIROOT = os.getenv("YUI_ROOT")
SITEDB = 'https://cmsweb.cern.ch/sitedb/json/index/CEtoCMSName?name'
reqMgrHost = "http://127.0.0.1:%d" % PORT

if re.match(r"^vocms(?:10[67]|5[03])\.cern\.ch$", HOST):
  HOST = "cmsweb.cern.ch"
  COUCH = "http://vocms53.cern.ch:5984"
elif re.match(r"^vocms(?:51|13[23])\.cern\.ch$", HOST):
  HOST = "cmsweb-testbed.cern.ch"
  COUCH = "http://vocms133.cern.ch:5984"

config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

config.section_("CoreDatabase")
config.CoreDatabase.connectUrl = connectUrl

config.component_("Webtools")
config.Webtools.host = '0.0.0.0'
config.Webtools.port = PORT
config.Webtools.application = "ReqMgr"

config.component_('ReqMgr')
config.webapp_("ReqMgr")
config.ReqMgr.componentDir = BASEDIR + "/var"
config.ReqMgr.database.connectUrl = connectUrl
config.ReqMgr.templates = TEMPLATES
config.ReqMgr.admin = 'cms-service-webtools@cern.ch'
config.ReqMgr.title = 'CMS Request Manager'
config.ReqMgr.description = 'CMS Request manager'
config.ReqMgr.couchUrl = COUCH
config.ReqMgr.configDBName = 'reqmgr_config_cache'
config.ReqMgr.yuiroot = YUIROOT

views = config.ReqMgr.section_('views')
active = views.section_('active')

active.section_('reqMgr')
active.reqMgr.section_('model')
active.reqMgr.section_('formatter')
active.reqMgr.object = 'WMCore.WebTools.RESTApi'
active.reqMgr.model.object = 'WMCore.HTTPFrontEnd.RequestManager.ReqMgrRESTModel'
active.reqMgr.model.reqMgrHost = reqMgrHost
active.reqMgr.model.couchUrl = COUCH
active.reqMgr.model.workloadCouchDB = 'wmagent_workload_cache'
active.reqMgr.default_expires = 0 # no caching
active.reqMgr.formatter.object = 'WMCore.WebTools.RESTFormatter'

active.section_('view')
active.view.object = 'WMCore.HTTPFrontEnd.RequestManager.ReqMgrBrowser'
active.view.reqMgrHost = reqMgrHost

active.section_('admin')
active.admin.object = 'WMCore.HTTPFrontEnd.RequestManager.Admin'

active.section_('approve')
active.approve.object = 'WMCore.HTTPFrontEnd.RequestManager.Approve'

active.section_('assign')
active.assign.object = 'WMCore.HTTPFrontEnd.RequestManager.Assign'
active.assign.sitedb = SITEDB

active.section_('create')
active.create.object = 'WMCore.HTTPFrontEnd.RequestManager.WebRequestSchema'
active.create.requestor = 'rpw'
active.create.reqMgrHost = reqMgrHost
active.create.cmsswDefaultVersion = 'CMSSW_3_5_8'

active.section_('RequestOverview')
active.RequestOverview.object = 'WMCore.HTTPFrontEnd.RequestManager.RequestOverview'
active.RequestOverview.templates = TEMPLATES
active.RequestOverview.javascript = os.path.join(getWMBASE(), 'javascript')
active.RequestOverview.html = os.path.join(getWMBASE(), 'html')
