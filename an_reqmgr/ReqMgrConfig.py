import os, re, socket, thread
__all__ = []
from WMCore.WMInit import getWMBASE
from WMCore.Configuration import Configuration
from ReqMgrSecrets import connectUrl

#
# Configuration that matters
#
HOST = socket.getfqdn().lower()
PORT = 8245
COUCH = "https://%s/couchdb" % HOST
if re.match(r"^vocms(?:13[689]|140|16[13])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb.cern.ch/couchdb"
elif re.match(r"^vocms(?:13[23])\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-testbed.cern.ch/couchdb"
elif re.match(r"^vocms127\.cern\.ch$", HOST):
  COUCH = "https://cmsweb-dev.cern.ch/couchdb"

configCouchDB = 'analysis_reqmgr_config_cache'
workloadCouchDB = 'analysis_reqmgr_workload_cache'
workloadSummaryCouchDB = "analysis_workloadsummary"
wmstatCouchDB = "analysis_wmstats"
sitedb = 'https://cmsweb.cern.ch/sitedb/json/index/CEtoCMSName?name'
dbs3 = 'http://vocms09.cern.ch:8989/dbs'
yuiroot = "/an_reqmgr/yuiserver/yui"

INSTALL = getWMBASE()
TEMPLATES = os.path.normpath(os.path.join(INSTALL, '../../../data/templates/WMCore/WebTools'))
JAVASCRIPT_PATH = os.path.normpath(os.path.join(INSTALL, '../../../data/javascript'))
HTML_PATH = os.path.normpath(os.path.join(INSTALL, '../../../data/html'))
SECURITY_ROLES = ['Admin', 'Developer', 'Data Manager', 'developer', 'admin', 'data-manager', 'facops', 'FacOps']

#
# Beginning of the boilerplate configuration bits
#
config = Configuration()

config.component_("Webtools")
config.Webtools.host = '0.0.0.0'
config.Webtools.port = PORT
config.Webtools.application = "an_reqmgr"
config.Webtools.environment = 'production'
#config.Webtools.environment = 'development'
config.Webtools.proxy_base = 'True'
config.Webtools.thread_pool = 30
thread.stack_size(128*1024)

config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

config.component_('an_reqmgr')
config.section_("CoreDatabase")
config.CoreDatabase.connectUrl = connectUrl
config.an_reqmgr.section_('database')
config.an_reqmgr.database.connectUrl = connectUrl
config.an_reqmgr.componentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/var"
config.an_reqmgr.templates = os.path.join(TEMPLATES, 'RequestManager')
config.an_reqmgr.html = os.path.join(HTML_PATH, 'RequestManager')
config.an_reqmgr.javascript = JAVASCRIPT_PATH
config.an_reqmgr.admin = 'cms-service-webtools@cern.ch'
config.an_reqmgr.title = 'CMS Request Manager'
config.an_reqmgr.description = 'CMS Request Manager'
config.an_reqmgr.couchUrl = COUCH
config.an_reqmgr.configDBName = configCouchDB
config.an_reqmgr.workloadDBName = workloadCouchDB
config.an_reqmgr.wmstatDBName = wmstatCouchDB
config.an_reqmgr.security_roles = SECURITY_ROLES
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
active.assign.opshold = False
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
active.reqMgr.templates = TEMPLATES
active.reqMgr.html = os.path.join(HTML_PATH, 'RequestManager')

active.section_('rest')
active.rest.section_('model')
active.rest.section_('formatter')
active.rest.object = 'WMCore.WebTools.RESTApi'
active.rest.model.object = 'WMCore.HTTPFrontEnd.RequestManager.ReqMgrRESTModel'
active.rest.default_expires = 0 # no caching
active.rest.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.rest.templates = TEMPLATES

active.section_('create')
active.create.object = 'WMCore.HTTPFrontEnd.RequestManager.WebRequestSchema'
active.create.requestor = None
active.create.cmsswDefaultVersion = 'CMSSW_5_2_5'

active.section_('yuiserver')
active.yuiserver.object = 'WMCore.WebTools.YUIServer'
active.yuiserver.yuidir = os.getenv("YUI_ROOT")
