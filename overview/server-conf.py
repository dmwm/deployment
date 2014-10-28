import os, os.path
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = CONFIGDIR.replace("/current/config/overview", "")
STATEDIR  = "%s/state/overview" % BASEDIR
LOGDIR    = "%s/logs/overview" % BASEDIR
AUTHDIR   = "%s/current/auth/overview" % BASEDIR

modules = ("Monitoring.Core.Cache",
           "Monitoring.Overview.ProdMon",
           "Monitoring.Overview.FileLight",
           "Monitoring.Overview.PhEDEx",
           "Monitoring.Overview.Core",
           "Monitoring.Overview.DDT",
           "Monitoring.Overview.Grid",
           "Monitoring.Overview.Tier0",
           "Monitoring.Overview.Welcome",
           "Monitoring.Overview.CAF")

server.port        = 9000
server.serverDir   = STATEDIR
server.logFile     = '%s/weblog-%%Y%%m%%d.log' % LOGDIR
server.baseUrl     = '/overview'
server.title       = 'CMS computing'
server.serviceName = 'Computing overview'
server.options     = { 'thread_pool': 25, 'stack_size': 512*1024 }

server.service('Computing overview', 'http://cmsweb.cern.ch/overview')
server.service('Computing overview test', 'http://vocms0127.cern.ch/overview')

server.source('ProdMon')
server.source('FileLight')
server.source('PhEDEx', '%s/dbparam.py' % AUTHDIR)
server.source('CAFPlot')
server.source('CAFDisk',
		('alca', r"alca"),
		('comm', r"^(/calo/|/minimumbias/|/monitor/|/testenables/"
			"|/hltdebug/|/hcalhpdnoise/|/randomtriggers/"
			"|/test/commissioning|/calprivate|/barrelmuon/"
			"|/endcapsmuon/|/minbias/|/[^/]*(cosmic|beamhalo)"
			"|/global[^/]*-A/)"),
		('phys', '^'))
server.source('CompDDT')
server.source('CompTier0')

server.workspace('CompWelcome',  10, 'Shift',     'Welcome')
server.workspace('CompCore',     11, 'Shift',     'CERN/Core')
server.workspace('CompCAF',      13, 'Shift',     'CAF')
server.workspace('CompDDT',      14, 'Shift',     'Transfers')
server.workspace('CompGrid',     15, 'Shift',     'Grid Services')
server.workspace('CompPhEDEx',   20, 'Activity',  'PhEDEx')
server.workspace('FileLight',    21, 'Activity',  'FileLight')
server.workspace('ProdMon',      22, 'Activity',  'Prodmon')

server.extend('OverviewCache')
