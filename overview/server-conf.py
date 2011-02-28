import os, os.path
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
SWDIR = os.path.normcase(os.environ["OVERVIEW_ROOT"]).rsplit('/', 3)[0]
SRVDIR = '/data/state/overview'
AUTHDIR = '/data/current/auth/overview'

modules = ("GuiProdmon", "GuiCache", "GuiFilelight", "GuiCompPhedex", "GuiCompCore",
           "GuiCompDDT", "GuiCompGrid", "GuiCompTier0", "GuiCompWelcome", "GuiCompCAF")

envsetup = """
  export EXTJS_ROOT=%(SWDIR)s/external/extjs/3.1.1
  export MPLCONFIGDIR=%(SRVDIR)s
  export MATPLOTLIBRC=%(CONFIGDIR)s
  export TNS_ADMIN=%(CONFIGDIR)s
  export HOME=%(CONFIGDIR)s
  export QUIET_ASSERT=a
""" % locals()

server.port        = 9000
server.serverDir   = SRVDIR
server.baseUrl     = '/overview'
server.title       = 'CMS computing'
server.serviceName = 'Computing overview'
server.options     = { 'thread_pool': 25, 'stack_size': 512*1024 }

server.service('Computing overview', 'http://cmsweb.cern.ch/overview')
server.service('Computing overview test', 'http://vocms109.cern.ch/overview')

server.source('Prodmon')
server.source('Filelight')
server.source('Phedex', '%s/dbparam.py' % AUTHDIR)
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
server.workspace('CompTier0',    12, 'Shift',     'Tier-0')
server.workspace('CompCAF',      13, 'Shift',     'CAF')
server.workspace('CompDDT',      14, 'Shift',     'Transfers')
server.workspace('CompGrid',     15, 'Shift',     'Grid Services')
server.workspace('CompPhedex',   20, 'Activity',  'PhEDEx')
server.workspace('Filelight',    21, 'Activity',  'Filelight')
server.workspace('Prodmon',      22, 'Activity',  'Prodmon')

server.extend('OverviewCache')
