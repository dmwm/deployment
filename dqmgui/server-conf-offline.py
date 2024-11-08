import os.path, socket

global CONFIGDIR
from glob import glob

CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit("/", 1)[0]
BASEDIR = __file__.rsplit("/", 4)[0]
STATEDIR = "%s/state/dqmgui/offline" % BASEDIR
LOGDIR = "%s/logs/dqmgui/offline" % BASEDIR

LAYOUTS = glob("%s/layouts/shift_*_T0_layout.py" % CONFIGDIR)
LAYOUTS += glob("%s/layouts/*_overview_layouts.py" % CONFIGDIR)
LAYOUTS += glob("%s/layouts/*_T0_layouts.py" % CONFIGDIR)

modules = ("Monitoring.DQM.GUI",)

# server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
# server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
# server.instrument  = 'igprof -d -t python -pp'
# server.instrument  = 'igprof -d -t python -mp'
server.port = 8080
server.serverDir = STATEDIR
# For convenience, we change some config, depending on the server:
hostname = socket.gethostname().lower().split(".")[0]
server.logFile = "%s/weblog.log" % LOGDIR
server.title = "CMS data quality"

# Offline production servers
if hostname == "vocms0736":
    server.serviceName = "Offline"
    server.baseUrl = "/dqm/offline"
# Relval test server
elif hostname == "vocms0730":
    server.serviceName = "Offline Test"
    server.baseUrl = "/dqm/offline-test"
# Any local instance of the relval flavor
else:
    server.serviceName = "Offline Local"
    server.baseUrl = "/dqm/offline"

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
        "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=dpapagia/CN=857294/CN=Dimitrios Papagiannis",
        "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=dpapagia/CN=857294/CN=Dimitris Papagiannis",
        "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=gamoreir/CN=844403/CN=Gabriel Moreira Da Silva Campos",
    ],
)
server.source("DQMUnknown")
server.source("DQMOverlay")
server.source("DQMStripChart")
server.source("DQMCertification")
server.source("DQMArchive", "%s/ix128" % STATEDIR, "^/Global/")
server.source("DQMLayout")

exec(open(os.path.join(CONFIGDIR, "dqm-services.py")).read())
exec(open(os.path.join(CONFIGDIR, "workspaces-offline.py")).read())
