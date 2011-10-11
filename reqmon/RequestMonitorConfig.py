__all__ = []
import os, re, socket
from WMCore.WMInit import getWMBASE
from WMCore.Configuration import Configuration
import os.path
INSTALL = getWMBASE()

#REQ_MGR_URL = "%s/%s" % (getURLBYHost(), "reqmgr/reqMgr")
#WORKLOAD_COUCH = "%s/%s" % (getURLBYHost(), "couchdb/workloadsummary")
REQ_MGR_URL = "https://cmsweb.cern.ch/reqmgr/rest"
WORKLOAD_COUCH = "https://cmsweb.cern.ch/couchdb/workloadsummary"
SERVICE_LEVEL = "RequestManager"

TEMPLATES = os.path.normpath(os.path.join(INSTALL, '../../templates/WMCore/WebTools'))
JAVASCRIPT_PATH = os.path.normpath(os.path.join(INSTALL, '../../javascript'))
HTML_PATH = os.path.normpath(os.path.join(INSTALL, '../../html'))

config = Configuration()

config.component_("Webtools")
config.Webtools.host = '0.0.0.0'
#use teh same port as reqmgr due to the frontend server.conf.
#if different fort is needed change the fronted server.conf
config.Webtools.port = 8240
config.Webtools.application = "reqmgr"
config.Webtools.proxy_base = 'True'
config.Webtools.thread_pool = 30
config.Webtools.environment = 'production'
#config.Webtools.environment = 'development'

config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

config.component_('reqmgr')
config.reqmgr.admin = 'cms-service-webtools@cern.ch'
config.reqmgr.title = 'CMS Request Monitor'
config.reqmgr.description = 'CMS Request Monitor'
#config.reqmgr.section_('database')
#config.reqmgr.database.connectUrl = "sqlplus://user:pass@nodb"
active = config.reqmgr.section_('views').section_('active')

active.section_('GlobalMonitor')
active.GlobalMonitor.object = 'WMCore.HTTPFrontEnd.GlobalMonitor.GlobalMonitorPage'
active.GlobalMonitor.templates = TEMPLATES
active.GlobalMonitor.javascript = JAVASCRIPT_PATH
active.GlobalMonitor.html = HTML_PATH
active.GlobalMonitor.serviceLevel = SERVICE_LEVEL

active.section_('monitorSvc')
active.monitorSvc.serviceURL = REQ_MGR_URL
active.monitorSvc.serviceLevel = SERVICE_LEVEL
active.monitorSvc.workloadSummaryCouchURL = WORKLOAD_COUCH
active.monitorSvc.section_('model')
active.monitorSvc.section_('formatter')
active.monitorSvc.object = 'WMCore.WebTools.RESTApi'
active.monitorSvc.model.object = 'WMCore.HTTPFrontEnd.GlobalMonitor.GlobalMonitorRESTModel'
active.monitorSvc.default_expires = 0 # no caching
active.monitorSvc.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.monitorSvc.template = TEMPLATES
