import os.path, socket; global CONFIGDIR
from glob import glob
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = CONFIGDIR.replace("/current/config/dqmgui", "")
STATEDIR  = "%s/state/dqmgui/caf" % BASEDIR
LOGDIR    = "%s/logs/dqmgui/caf" % BASEDIR

LAYOUTS = glob("%s/layouts/*_caf_layouts.py" % CONFIGDIR)
LAYOUTS += glob("%s/layouts/shift_*_caf_layouts.py" % CONFIGDIR)

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
server.extend('DQMFileAccess', "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0],
              "%s/uploads" % STATEDIR,
              { "ROOT": "%s/data" % STATEDIR,
                "CAF": "%s/data" % STATEDIR, # legacy
                "ZIP": "%s/zipped" % STATEDIR })
server.extend('DQMLayoutAccess', None, STATEDIR,
              ['/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=rovere/CN=653292/CN=Marco Rovere',
               '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=batinkov/CN=739757/CN=Atanas Ivanov Batinkov',
               '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=bvanbesi/CN=759373/CN=Broen van Besien',])
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')
server.source('DQMArchive', "%s/ix128" % STATEDIR, '^/Global/')
server.source('DQMLayout')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-caf.py")
