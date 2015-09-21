from WMCore.Configuration import Configuration

config = Configuration()

# web_server configuration
config.component_('web_server')
config.web_server.thread_pool = 150
config.web_server.socket_queue_size = 100
config.web_server.timeout_monitor = False
config.web_server.loglevel = 0
config.web_server.host = '0.0.0.0'
config.web_server.log_screen = True
config.web_server.url_base = '/das'
config.web_server.logfile = ''
config.web_server.port = 8211
config.web_server.pid = '%s/state/das/das_cli_server.pid' % __file__.rsplit('/', 4)[0]
config.web_server.status_update = 2500
config.web_server.web_workers = 50
config.web_server.queue_limit = 1000
config.web_server.qtype = 'Queue'
config.web_server.adjust_input = True
config.web_server.dbs_daemon = False # disable DBS daemon, it will run in das web server
config.web_server.hot_threshold = 3000
config.web_server.services = ['dbs_phedex']
config.web_server.check_clients = False # set True when DAS ready

# cache requests configuration
config.component_('cacherequests')
config.cacherequests.Admin = 50
config.cacherequests.Unlimited = 10000
config.cacherequests.ProductionAccess = 5000

# mongodb configuration
config.component_('mongodb')
config.mongodb.bulkupdate_size = 5000
config.mongodb.dburi = ['mongodb://localhost:8230']
config.mongodb.lifetime = 300
config.mongodb.dbname = 'das'

# pycurl configuration
config.component_('pycurl')
config.pycurl.FOLLOWLOCATION=1
config.pycurl.CONNECTTIMEOUT=270
config.pycurl.MAXREDIRS=5
config.pycurl.NOSIGNAL=1
config.pycurl.TIMEOUT=270
config.pycurl.SSL_VERIFYPEER=False
config.pycurl.VERBOSE=0

# dasdb configuration
config.component_('dasdb')
config.dasdb.dbname = 'das'
config.dasdb.cachecollection = 'cache'
config.dasdb.mergecollection = 'merge'
config.dasdb.mrcollection = 'mapreduce'
config.dasdb.logging = False
config.dasdb.record_ttl = 86400
config.dasdb.delta_ttl = 60
config.dasdb.cleanup_worker = True
config.dasdb.cleanup_interval = 600
config.dasdb.cleanup_delta_ttl = 3600

# mappingdb configuration
config.component_('mappingdb')
config.mappingdb.collname = 'db'
config.mappingdb.dbname = 'mapping'
config.mappingdb.reload_time = 3600

# parserdb configuration
config.component_('parserdb')
config.parserdb.dbname = 'parser'
config.parserdb.collname = 'db'
config.parserdb.enable = True
config.parserdb.sizecap = 5242880

# das configuration
config.component_('das')
config.das.logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
config.das.logfile = ''
config.das.verbose = 0
config.das.multitask = True
config.das.core_workers = 50
config.das.api_workers = 2
config.das.error_expire = 300
config.das.emptyset_expire = 5
config.das.parserdir = '%s/state/das' % __file__.rsplit('/', 4)[0] # area owned by _das account
config.das.services = ['dbs3','phedex','dashboard','monitor','runregistry','sitedb2','combined','conddb','reqmgr','mcm']
config.das.main_dbs = 'dbs3'

# keyword search configuration
config.component_('keyword_search')
config.keyword_search.kws_on = False # disable ajax client
config.keyword_search.kws_service_on = False # disable ajax server

# query rewriting configuration
config.component_('query_rewrite')
config.query_rewrite.pk_rewrite_on = False
