import os.path, socket; global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = CONFIGDIR.replace("/current/config/dqmgui", "")
STATEDIR  = "%s/state/dqmgui/offline" % BASEDIR
LOGDIR    = "%s/logs/dqmgui/offline" % BASEDIR

LAYOUTS = ["%s/layouts/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in
           ("castor","eb", "ee", "es", "csc", "rpc", "hcal", "hcalcalib", "l1t", "l1temulator", "hlt", "pixel", "sistrip", "dt", "muons", "jetmet", "egamma")]
LAYOUTS += ["%s/layouts/%s_overview_layouts.py" % (CONFIGDIR, x) for x in
            ("sistrip","ecal","hcal","beammonitor","l1t","hlt")]
LAYOUTS += ["%s/layouts/%s_T0_layouts.py" % (CONFIGDIR, x) for x in
           ("btag","castor","csc","pixel","sistrip","hcal", "hcalcalib", "eb", "ee", "es", "hltmuon", "rpc")]

modules = ("Monitoring.DQM.GUI",)

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
#server.instrument  = 'igprof -d -t python -mp'
server.port        = 8080
server.serverDir   = STATEDIR
server.logFile     = '%s/weblog-%%Y%%m%%d.log' % LOGDIR
server.baseUrl     = '/dqm/offline'
server.title       = 'CMS data quality'
server.serviceName = 'Offline'

server.plugin('render', "%s/style/*.cc" % CONFIGDIR)
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMToJSON')
server.extend('DQMFileAccess', None, "%s/uploads" % STATEDIR,
              { "ROOT": "%s/data" % STATEDIR,
                "ZIP": "%s/zipped" % STATEDIR })
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')
server.source('DQMArchive', "%s/ix" % STATEDIR, '^/Global/')
server.source('DQMLayout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
