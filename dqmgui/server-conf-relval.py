import os.path, socket; global CONFIGDIR
from glob import glob
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = CONFIGDIR.replace("/current/config/dqmgui", "")
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

modules = ("Monitoring.DQM.GUI",)

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
#server.instrument  = 'igprof -d -t python -mp'
server.port        = 8081
server.serverDir   = STATEDIR
server.logFile     = '%s/weblog-%%Y%%m%%d.log' % LOGDIR
server.baseUrl     = '/dqm/relval'
server.title       = 'CMS data quality'
server.serviceName = 'RelVal'

server.plugin('render', "%s/style/*.cc" % CONFIGDIR)
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMToJSON')
server.extend('DQMFileAccess', "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0],
              "%s/uploads" % STATEDIR,
              { "ROOT": "%s/data" % STATEDIR,
                "ZIP": "%s/zipped" % STATEDIR })
server.extend('DQMLayoutAccess', None, STATEDIR,
              ['/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=rovere/CN=653292/CN=Marco Rovere',
               '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=erosales/CN=725205/CN=Edgar Eduardo Rosales Rosero',
               '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=batinkov/CN=739757/CN=Atanas Ivanov Batinkov' ])
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')

# Switch to use the new index schema only on vocms139. If users want
# to test the relval server configuration on their local machine, they
# are still able to do that using the old schema.

if socket.gethostname().lower().split('.')[0] in ['vocms139','vocms0139']  :
    server.source('DQMArchive', "%s/ix128" % STATEDIR, '^/Global/')
else:
    server.source('DQMArchive', "%s/ix" % STATEDIR, '^/Global/')
server.source('DQMLayout')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-relval.py")
