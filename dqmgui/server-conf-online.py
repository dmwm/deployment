import os.path, socket; global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = CONFIGDIR.replace("/current/config/dqmgui", "")
STATEDIR  = "%s/state/dqmgui" % BASEDIR
LOGDIR    = "%s/logs/dqmgui" % BASEDIR

# Modifiable parameters.
LAYOUTS = ["%s/layouts/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("castor","csc", "dt", "eb", "ee", "es","hcal", "hcalcalib", "hlt", "hlx", "l1t", "l1temulator", "rpc", "pixel", "sistrip", "sistriplas")]
LAYOUTS += ["%s/layouts/%s_overview_layouts.py" % (CONFIGDIR, x) for x in
            ("sistrip","ecal","hcal","beammonitor","l1t","hlt")]
LAYOUTS += ["%s/layouts/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("beam","castor","csc", "dt", "eb", "ee", "error", "es","hcal", "hlt", "info", "l1t", "rpc", "pixel", "sistrip" , "fed" )]

# Do not modify configuration below this line.
HOST      = socket.gethostname().lower()
HOSTADDR  = socket.getaddrinfo(HOST, None)[0][4][0]
BASEDIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOSTALIAS = HOST
COLLHOST  = (HOST.find("-c2d07-01") > 0 and 'localhost') or 'dqm-c2d07-01'

# Figure out a preferred alias for this out (if any)
for alias in ["dqm-prod-local", "dqm-prod-offsite", "dqm-integration", "dqm-test"]:
  if len([x for x in socket.getaddrinfo(alias, None) if x[4][0] == HOSTADDR]):
    HOSTALIAS = alias
    break

# Server configuration.
modules = ("Monitoring.DQM.GUI",)

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
#server.instrument  = 'igprof -d -t python -mp'
server.localBase   = HOSTALIAS
server.serverDir   = STATEDIR
server.logFile     = '%s/weblog-%%Y%%m%%d.log' % LOGDIR
server.baseUrl     = '/dqm/online'
server.title       = 'CMS data quality'
server.serviceName = 'Online'

server.plugin('render', "%s/style/*.cc" % CONFIGDIR)
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMToJSON')
server.extend('DQMFileAccess', None, "/dqmdata/dqm/uploads",
              { "ROOT": "/dqmdata/dqm/repository/original/OnlineData",
                "Original": "/dqmdata/dqm/repository/original/OnlineData",
                "Merged": "/dqmdata/dqm/repository/merged/OnlineData" }) # legacy
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')
server.source('DQMLive', "%s:9090" % COLLHOST)
server.source('DQMArchive', "%s/ix" % STATEDIR, '^/Global/')
server.source('DQMLayout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
