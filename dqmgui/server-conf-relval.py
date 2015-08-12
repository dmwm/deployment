import os.path, socket; global CONFIGDIR
from glob import glob
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = __file__.rsplit('/', 4)[0]
STATEDIR  = "%s/state/dqmgui/relval" % BASEDIR
LOGDIR    = "%s/logs/dqmgui/relval" % BASEDIR

LAYOUTS = glob("%s/layouts/shift_%s_relval_layout.py" % (CONFIGDIR, "hlt"))
LAYOUTS += glob("%s/layouts/shift_%s_relval_layout.py" % (CONFIGDIR, "ecal"))
LAYOUTS += glob("%s/layouts/shift_%s_relval_layout.py" % (CONFIGDIR, "pflow"))
LAYOUTS += glob("%s/layouts/%smc_relval-layouts.py" % (CONFIGDIR, "ecal"))
LAYOUTS += glob("%s/layouts/%smc_relval-layouts.py" % (CONFIGDIR, "tk"))
LAYOUTS += glob("%s/layouts/%smc_relval-layouts.py" % (CONFIGDIR, "pflow"))
LAYOUTS += glob("%s/layouts/%s_relval-layouts.py" % (CONFIGDIR, "hlt"))
LAYOUTS += glob("%s/layouts/%s_relval-layouts.py" % (CONFIGDIR, "ecal"))
LAYOUTS += glob("%s/layouts/%s_relval-layouts.py" % (CONFIGDIR, "tk"))
LAYOUTS += glob("%s/layouts/%s_relval-layouts.py" % (CONFIGDIR, "smp"))

modules = ("Monitoring.DQM.GUI",)

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
#server.instrument  = 'igprof -d -t python -mp'
server.port        = 8081
server.serverDir   = STATEDIR
server.logFile     = '%s/weblog-%%Y%%m%%d.log' % LOGDIR
server.title       = 'CMS data quality'
# For convenience, we change the service name, depending on the server:
hostname = socket.gethostname().lower().split('.')[0]
# Relval production server
if hostname == 'vocms0139':
  server.serviceName = 'RelVal'
  server.baseUrl     = '/dqm/relval'
# Relval test server
elif hostname == 'vocms0131':
  server.serviceName = 'RelVal Test'
  server.baseUrl     = '/dqm/relval-test'
# Any local instance of the relval flavor
else:
  server.serviceName = 'RelVal Local'
  server.baseUrl     = '/dqm/relval'

server.plugin('render', "%s/style/*.cc" % CONFIGDIR)
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMToJSON')
server.extend('DQMFileAccess', "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0],
              "%s/uploads" % STATEDIR,
              { "ROOT": "%s/data" % STATEDIR,
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
execfile(CONFIGDIR + "/workspaces-relval.py")
