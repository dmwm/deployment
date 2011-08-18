import os.path, socket; global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = CONFIGDIR.replace("/current/config/dqmgui", "")
STATEDIR  = "%s/state/dqmgui/caf" % BASEDIR
LOGDIR    = "%s/logs/dqmgui/caf" % BASEDIR

LAYOUTS = ["%s/layouts/%s_caf_layouts.py" % (CONFIGDIR, x) for x in
	   ("tkal",)]

modules = ("Monitoring.DQM.GUI",)

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
#server.instrument  = 'igprof -d -t python -mp'
server.port        = 8040
server.serverDir   = STATEDIR
server.logFile     = '%s/weblog-%%Y%%m%%d.log' % LOGDIR
server.baseUrl     = '/dqm/caf'
server.title       = 'CMS data quality'
server.serviceName = 'CERN CAF'

server.plugin('render', "%s/style/*.cc" % CONFIGDIR)
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMToJSON')
server.extend('DQMFileAccess', None, "%s/uploads" % STATEDIR,
              { "ROOT": "%s/data" % STATEDIR,
                "CAF": "%s/data" % STATEDIR, # legacy
                "ZIP": "%s/zipped" % STATEDIR })
server.extend('DQMLayoutAccess', None, "%s/layouts" % STATEDIR,
              ['/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=lilopera/CN=692665/CN=Luis Ignacio Lopera Gonzalez',
               '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=rovere/CN=653292/CN=Marco Rovere' ])
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')
server.source('DQMArchive', "%s/ix" % STATEDIR, '^/Global/')
server.source('DQMLayout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-caf.py")
