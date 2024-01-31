import os.path, socket

global CONFIGDIR
from glob import glob

CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit("/", 1)[0]
BASEDIR = __file__.rsplit("/", 4)[0]
STATEDIR = "%s/state/dqmgui/dev" % BASEDIR
LOGDIR = "%s/logs/dqmgui/dev" % BASEDIR

LAYOUTS = glob("%s/layouts/shift_*_T0_layout.py" % CONFIGDIR)
LAYOUTS += glob("%s/layouts/*_T0_layouts.py" % CONFIGDIR)
LAYOUTS += glob("%s/*_overview_layouts.py" % CONFIGDIR)
LAYOUTS += glob("%s/layouts/shift_*_relval_layout.py" % CONFIGDIR)
LAYOUTS += glob("%s/layouts/*_relval-layouts.py" % CONFIGDIR)

modules = ("Monitoring.DQM.GUI",)
hostname = socket.gethostname().lower().split(".")[0]

# server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
# server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
# server.instrument  = 'igprof -d -t python -pp'
# server.instrument  = 'igprof -d -t python -mp'
server.port = 8060
server.serverDir = STATEDIR
server.logFile = (
    # TODO: Remove after migration of vocms machines to newer OS (>=RHEL8).
    "%s/weblog-%%Y%%m%%d.log" % LOGDIR
    if "vocms" in hostname
    else "%s/weblog.log" % LOGDIR
)
server.baseUrl = "/dqm/dev"
server.title = "CMS data quality"
server.serviceName = "CERN Development"

server.plugin("render", "%s/style/*.cc" % CONFIGDIR, "%s/style/*.h" % CONFIGDIR)
server.extend("DQMRenderLink", server.pathOfPlugin("render"))
server.extend("DQMToJSON")
server.extend(
    "DQMFileAccess",
    "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit("/", 3)[0],
    "%s/uploads" % STATEDIR,
    {"ROOT": "%s/data" % STATEDIR, "ZIP": "%s/zipped" % STATEDIR},
)
server.extend(
    "DQMLayoutAccess",
    None,
    STATEDIR,
    [
        "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=rovere/CN=653292/CN=Marco Rovere",
        "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=batinkov/CN=739757/CN=Atanas Ivanov Batinkov",
        "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=bvanbesi/CN=759373/CN=Broen van Besien",
    ],
)
server.source("DQMUnknown")
server.source("DQMOverlay")
server.source("DQMStripChart")
server.source("DQMCertification")
server.source("DQMLive", "127.0.0.1:8061")
server.source("DQMArchive", "%s/ix128" % STATEDIR, "^/Global/")
# Layouts are disabled because dev gui is used for visualising PR test bin by bin comparison output.
# Uncomment the following line to enable layouts:
# server.source('DQMLayout')

exec(open(os.path.join(CONFIGDIR, "dqm-services.py")).read())
exec(open(os.path.join(CONFIGDIR, "workspaces-dev.py")).read())
