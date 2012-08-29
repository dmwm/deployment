import thread
thread.stack_size(128*1024)

import os, re, socket
__all__ = []
from WMCore.WMInit import getWMBASE
from WMCore.Configuration import Configuration

INSTALL = getWMBASE()
HOST = socket.getfqdn().lower()
COUCH = "https://%s/couchdb" % HOST
PORT = 8245

if re.match(r"^vocms(?:10[67]|13[689]|140|16[13])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb.cern.ch/couchdb"
elif re.match(r"^vocms(?:13[23])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-testbed.cern.ch/couchdb"
elif re.match(r"^vocms127\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-dev.cern.ch/couchdb"

componentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/var"
reqMgrHost = "http://%s:%d" % (socket.gethostname().lower(), 8245)

configCouchDB = 'analysis_reqmgr_config_cache'
workloadCouchDB = 'analysis_reqmgr_workload_cache'
workloadSummaryCouchDB = "analysis_workloadsummary"
wmstatCouchDB = "analysis_wmstats"
sitedb = 'https://cmsweb.cern.ch/sitedb/json/index/CEtoCMSName?name'
dbs3 = 'http://vocms09.cern.ch:8989/dbs'
yuiroot = "/an_reqmgr/yuiserver/yui"

TEMPLATES = os.path.normpath(os.path.join(INSTALL, '../../../data/templates/WMCore/WebTools'))
JAVASCRIPT_PATH = os.path.normpath(os.path.join(INSTALL, '../../../data/javascript'))
HTML_PATH = os.path.normpath(os.path.join(INSTALL, '../../../data/html'))

reqMgrHtml = os.path.normpath(os.path.join(INSTALL, '../../../data/html/RequestManager'))
reqMgrTemplates = os.path.normpath(os.path.join(INSTALL, '../../../data/templates/WMCore/WebTools/RequestManager'))
reqMgrJavascript = os.path.normpath(os.path.join(INSTALL, '../../../data/javascript'))

config = Configuration()

config.component_("Webtools")
config.Webtools.host = '0.0.0.0'
config.Webtools.port = 8245
config.Webtools.application = "an_reqmgr"
config.Webtools.environment = 'production'
config.component_('an_reqmgr')
from ReqMgrSecrets import connectUrl
config.section_("CoreDatabase")
#read from Secrets file
config.CoreDatabase.connectUrl = connectUrl
config.an_reqmgr.section_('database')
config.an_reqmgr.database.connectUrl = connectUrl

config.an_reqmgr.componentDir = componentDir
config.an_reqmgr.templates = reqMgrTemplates
config.an_reqmgr.html = reqMgrHtml
config.an_reqmgr.javascript = reqMgrJavascript
config.an_reqmgr.admin = 'cms-service-webtools@cern.ch'
config.an_reqmgr.title = 'CMS Request Manager'
config.an_reqmgr.description = 'CMS Request Manager'
config.an_reqmgr.couchUrl = COUCH
config.an_reqmgr.configDBName = configCouchDB
config.an_reqmgr.workloadDBName = workloadCouchDB
config.an_reqmgr.wmstatDBName = wmstatCouchDB
config.an_reqmgr.security_roles = ['Admin', 'Developer', 'Data Manager', 'developer', 'admin', 'data-manager']
config.an_reqmgr.yuiroot = yuiroot
config.an_reqmgr.dbs3 = dbs3

views = config.an_reqmgr.section_('views')
active = views.section_('active')

active.section_('view')
active.view.object = 'WMCore.HTTPFrontEnd.RequestManager.ReqMgrBrowser'

active.section_('admin')
active.admin.object = 'WMCore.HTTPFrontEnd.RequestManager.Admin'
active.section_('approve')
active.approve.object = 'WMCore.HTTPFrontEnd.RequestManager.Approve'
active.section_('assign')
active.assign.object = 'WMCore.HTTPFrontEnd.RequestManager.Assign'
active.assign.sitedb = sitedb
# this value controls whether an assigned request will be put into
# ops-hold state and injected into OpsClipboard
active.assign.opshold = True
active.assign.clipboardDB = 'ops_clipboard'
active.section_('closeout')
active.closeout.object = 'WMCore.HTTPFrontEnd.RequestManager.CloseOut'
active.section_('announce')
active.announce.object = 'WMCore.HTTPFrontEnd.RequestManager.Announce'

active.section_('reqMgr')
active.reqMgr.section_('model')
active.reqMgr.section_('formatter')
active.reqMgr.object = 'WMCore.WebTools.RESTApi'
active.reqMgr.model.object = 'WMCore.HTTPFrontEnd.RequestManager.ReqMgrRESTModel'
active.reqMgr.default_expires = 0 # no caching
active.reqMgr.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.reqMgr.templates = os.path.join(INSTALL, 'data/templates/WMCore/WebTools')
#deprecate the old interface
active.section_('rest')
active.rest.section_('model')
active.rest.section_('formatter')
active.rest.object = 'WMCore.WebTools.RESTApi'
active.rest.model.object = 'WMCore.HTTPFrontEnd.RequestManager.ReqMgrRESTModel'
active.rest.default_expires = 0 # no caching
active.rest.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.rest.templates = os.path.join(INSTALL, 'data/templates/WMCore/WebTools')

active.section_('create')
active.create.object = 'WMCore.HTTPFrontEnd.RequestManager.WebRequestSchema'
active.create.requestor = None
active.create.cmsswDefaultVersion = 'CMSSW_5_2_5'

active.section_('yuiserver')
active.yuiserver.object = 'WMCore.WebTools.YUIServer'
active.yuiserver.yuidir = os.getenv("YUI_ROOT")

config.webapp_("an_reqmgr")
config.an_reqmgr.html = os.path.join(HTML_PATH, 'RequestManager')
config.an_reqmgr.templates = os.path.join(TEMPLATES, 'RequestManager')

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
