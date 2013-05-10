"""
ReqMgr only configuration file.
Everything configurable in ReqMgr is defined here.
"""
from WMCore.Configuration import Configuration
from os import path

config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "reqmgr2"
main.port = 8246 # main application port it listens on
main.index = "resthub"
# Defaults to allow any CMS authenticated user. Write APIs should require
# additional roles in SiteDB (i.e. "Admin" role for the "ReqMgr" group)
main.authz_defaults = {"role": None, "group": None, "site": None}

sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application) # string containing "reqmgr2"
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS data operations Request Manager."
app.title = "CMS Request Manager (ReqMgr)"

views = config.section_("views")

# redirector for the REST API implemented handlers
resthub = views.section_("resthub")
resthub.object = "WMCore.ReqMgr.service.hub.Hub"
# The couch host is defined during deployment time.
resthub.couch_host = @@COUCH_HOST@@
# practical to have this kind of configuration values not in
# service related RPM (difficult/impossible to change in CMS web
# deployment) but in the deployment configuration for the service
resthub.sitedb_url = "https://cmsweb.cern.ch/sitedb/json/index/CEtoCMSName?name"
# main ReqMgr CouchDB database containing all requests with spec files attached
resthub.couch_reqmgr_db = "reqmgr_workload_cache"
# ConfigCache - database with configuration documents
resthub.couch_config_cache_db = "reqmgr_config_cache"
resthub.couch_workload_summary_db = "workloadsummary"
resthub.couch_wmstats_db = "wmstats"
# number of past days since when to display requests in the default view
resthub.default_view_requests_since_num_days = 30 # days
"""
TODO:
- add info on meta-data database in couch (request states, teams, etc)
- add url to fetch users, roles, groups from sitedb (if necessary)
- add information about caching and page expiration
- active.create.cmsswDefaultVersion = 'CMSSW_5_2_5' should be configurable this way?
    (it's indeed used on the web GUI request create page)
"""
resthub.tag_collector_url = "https://cmstags.cern.ch/tc/ReleasesXML/?anytype=1"

# web user interface
ui = views.section_("ui")
ui.object = "WMCore.ReqMgr.webgui.frontpage.FrontPage"
ui.static_content_dir = path.join(path.abspath(__file__.rsplit('/', 3)[0]),"apps",main.application,"data")
