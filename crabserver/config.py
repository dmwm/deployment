from WMCore.Configuration import Configuration
from CRABServerAuth import connectUrl

conf = Configuration()
main = conf.section_('main')
srv = main.section_('server')
srv.thread_pool = 5
main.application = 'crabserver'
main.port = 8270
main.index = 'data'

main.authz_defaults = { 'role': None, 'group': None, 'site': None }
main.section_('tools').section_('cms_auth').key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

app = conf.section_('crabserver')
app.admin = 'marco.mascheroni@cern.ch'
app.description = 'CRABServer RESTFull API'
app.title = 'CRABRESTFull'

views = conf.section_('views')

data = views.section_('data')
data.object = 'CRABInterface.RESTBaseAPI.RESTBaseAPI'
data.monurl = 'http://localhost:5984'
data.monname = 'wmstats'
data.asomonurl = 'http://localhost:5984'
data.asomonname = 'user_monitoring_asynctransfer'
data.configcacheurl = 'https://cmsweb-testbed.cern.ch/couchdb'
data.configcachename = 'reqmgr_config_cache'
data.reqmgrurl = 'https://cmsweb-testbed.cern.ch/couchdb'
data.reqmgrname = 'reqmgr_workload_cache'
data.phedexurl = 'https://cmsweb.cern.ch/phedex/datasvc/xml/prod/'

data.connectUrl = connectUrl

conf.section_("CoreDatabase")
conf.CoreDatabase.connectUrl = connectUrl
