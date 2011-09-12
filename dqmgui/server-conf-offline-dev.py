import os.path, socket; global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = CONFIGDIR.replace("/current/config/dqmgui", "")
STATEDIR  = "%s/state/dqmgui/dev" % BASEDIR
LOGDIR    = "%s/logs/dqmgui/dev" % BASEDIR

LAYOUTS = ["%s/layouts/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in
           ("castor", "csc", "dt", "eb", "ee", "egamma", "es", "hcal", "hlt", "jetmet", "l1temulator", "l1t", "muons", "pixel", "rpc", "sistrip", "tracking")]
LAYOUTS += ["%s/layouts/%s_T0_layouts.py" % (CONFIGDIR, x) for x in
           ("btag", "castor", "csc", "eb", "ee", "es", "hcal", "hltmuon", "pixel", "rpc", "sistrip", "tracking")]
LAYOUTS += [CONFIGDIR + "/layouts/shift_hlt_relval_layout.py"]
LAYOUTS += [CONFIGDIR + "/layouts/hlt_relval-layouts.py"]

modules = ("Monitoring.DQM.GUI",)

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
#server.instrument  = 'igprof -d -t python -mp'
server.port        = 8060
server.serverDir   = STATEDIR
server.logFile     = '%s/weblog-%%Y%%m%%d.log' % LOGDIR
server.baseUrl     = '/dqm/dev'
server.title       = 'CMS data quality'
server.serviceName = 'CERN Development'

server.plugin('render', "%s/style/*.cc" % CONFIGDIR)
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMToJSON')
server.extend('DQMFileAccess', None, "%s/uploads" % STATEDIR,
              { "ROOT": "%s/data" % STATEDIR,
                "ZIP": "%s/zipped" % STATEDIR })
server.extend('DQMLayoutAccess', None, STATEDIR,
              ['/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=lilopera/CN=692665/CN=Luis Ignacio Lopera Gonzalez',
               '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=rovere/CN=653292/CN=Marco Rovere' ])
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')
server.source('DQMLive', "localhost:8061")
server.source('DQMArchive', "%s/ix" % STATEDIR, '^/Global/')
server.source('DQMLayout')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-dev.py")
