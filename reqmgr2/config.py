"""
ReqMgr only configuration file.
Everything configurable in ReqMgr is defined here.

"""

import socket
from WMCore.Configuration import Configuration
from os import path

HOST = socket.gethostname().lower()
ROOTDIR = __file__.rsplit('/', 3)[0]
config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "reqmgr2"
main.port = 8246 # main application port it listens on
main.index = "ui"
# Defaults to allow any CMS authenticated user. Write APIs should require
# additional roles in SiteDB (i.e. "Admin" role for the "ReqMgr" group)
main.authz_defaults = {"role": None, "group": None, "site": None}

sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application) # string containing "reqmgr2"
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS data operations Request Manager."
app.title = "CMS Request Manager (ReqMgr)"

views = config.section_("views")

# practical to have this kind of configuration values not in
# service related RPM (difficult/impossible to change in CMS web
# deployment) but in the deployment configuration for the service

# redirector for the REST API implemented handlers
data = views.section_("data")
data.object = "WMCore.ReqMgr.Service.RestApiHub.RestApiHub"
# The couch host is defined during deployment time.
data.couch_host = "@@COUCH_HOST@@"
# main ReqMgr CouchDB database containing all requests with spec files attached
data.couch_reqmgr_db = "reqmgr_workload_cache"
# ReqMgr database containing groups, teams, software, etc
data.couch_reqmgr_aux_db = "reqmgr_auxiliary"
# ConfigCache - database with configuration documents
data.couch_config_cache_db = "reqmgr_config_cache"
data.couch_workload_summary_db = "workloadsummary"
data.couch_wmstats_db = "wmstats"
data.couch_wmdatamining_db = "wmdatamining"
# number of past days since when to display requests in the default view
data.default_view_requests_since_num_days = 30 # days
# resource to fetch CMS software versions and scramarch info from
data.tag_collector_url = "https://cmssdt.cern.ch/SDT/cgi-bin/ReleasesXML?anytype=1"
# another source at TC, returns directly JSON, but strangely formatted (e.g.
# keys are not present at easy item but defined in a dedicated item ...)
# https://cmssdt.cern.ch/tc/getReleasesInformation?release_state=Announced

# request related settings (e.g. default injection arguments)
data.default_sw_version = "CMSSW_5_2_5"
data.default_sw_scramarch = "slc5_amd64_gcc434"
data.dqm_url = "https://cmsweb.cern.ch/dqm/dev"
data.dbs_url = "https://cmsweb.cern.ch/dbs/prod/global/DBSReader"

# web user interface
ui = views.section_("ui")
ui.static_content_dir = path.join(path.abspath(ROOTDIR),
                                 "apps",
                                 main.application,
                                 "data")
#ui.object = "WMCore.ReqMgr.WebGui.FrontPage.FrontPage"
ui.object = "WMCore.ReqMgr.Web.ReqMgrService.ReqMgrService"
ui.tmpldir = path.join(ui.static_content_dir, "html", "ReqMgr", "templates")
ui.imgdir = path.join(ui.static_content_dir, "html", "ReqMgr", "img")
ui.cssdir = path.join(ui.static_content_dir, "html", "ReqMgr", "style")
ui.jsdir = path.join(ui.static_content_dir, "html", "ReqMgr", "javascript")
#TODO : need to find correct location for this
ui.sdir = path.join(ui.static_content_dir, "html", "ReqMgr", "javascript")

ui.yuidir = path.join(ui.static_content_dir, "html", "ReqMgr", "yui")
ui.admin = 'cms-service-webtools@cern.ch'
ui.title = 'CMS ReqMgr Documentation'
ui.description = 'Documentation on the ReqMgrService'
ui.base = '/reqmgr2'
ui.index = 'reqmgr2' # this part must be activated, see below
ui.reqmgr = data # this part contains uiuration for ReqMgr REST API, see above
# This need to be removed when ReqMgr Client is removed
ui.reqmgr.reqmgr2_url = "https://reqmgr2-dev.cern.ch/reqmgr2" # this part contains uiuration for ReqMgr REST API, see above
ui_main = ui.section_("main")
ui_main.application = ui.index
#ui_main.authz_defaults = {"role": None, "group": None, "site": None, "policy": "dangerously_insecure"}


if  HOST.startswith("vocms0307"):
    extentions = config.section_("extensions")
    wmdatamining = extentions.section_("wmdatamining")
    wmdatamining.object = "WMCore.ReqMgr.CherryPyThreads.WMDataMining.WMDataMining"
    wmdatamining.wmstats_url = "https://cmsweb.cern.ch/couchdb/wmstats"
    wmdatamining.reqmgrdb_url = "https://cmsweb.cern.ch/couchdb/reqmgr_workload_cache"
    #wmdatamining.wmstats_url = "%s/%s" % (data.couch_host, data.couch_wmstats_db)
    #wmdatamining.reqmgrdb_url = "%s/%s" % (data.couch_host, data.couch_reqmgr_db)
    wmdatamining.mcm_url = "https://cms-pdmv.cern.ch/mcm"
    wmdatamining.mcm_cert = "%s/auth/reqmgr2/dmwm-service-cert.pem" % ROOTDIR
    wmdatamining.mcm_key = "%s/auth/reqmgr2/dmwm-service-key.pem" % ROOTDIR
    wmdatamining.mcm_tmp_dir = "%s/state/reqmgr2/tmp" % __file__.rsplit('/', 4)[0]
    wmdatamining.wmdatamining_url = "%s/%s" % (data.couch_host, data.couch_wmdatamining_db)
    wmdatamining.activeDuration = 60 * 15  # every 15 min
    wmdatamining.archiveDuration = 60 * 60 * 4 # every 4 hours
    
    # ACDC cleanup Thread
    couchCleanup = extentions.section_("couchCleanup")
    couchCleanup.object = "WMCore.ReqMgr.CherryPyThreads.CouchDBCleanup.CouchDBCleanup"
    couchCleanup.reqmgrdb_url = "https://cmsweb.cern.ch/couchdb/reqmgr_workload_cache"
    couchCleanup.acdc_url = "https://cmsweb.cern.ch/couchdb/acdcserver"
    couchCleanup.acdcCleanDuration = 60 * 60 * 4 # every 4 hours
    

#  for dev and vm use testbed data
if  HOST.startswith("vocms0133"):
    extentions = config.section_("extensions")
    wmdatamining = extentions.section_("wmdatamining")
    wmdatamining.object = "WMCore.ReqMgr.CherryPyThreads.WMDataMining.WMDataMining"
    wmdatamining.wmstats_url = "https://cmsweb-testbed.cern.ch/couchdb/wmstats"
    wmdatamining.reqmgrdb_url = "https://cmsweb-testbed.cern.ch/couchdb/reqmgr_workload_cache"
    #wmdatamining.wmstats_url = "%s/%s" % (data.couch_host, data.couch_wmstats_db)
    #wmdatamining.reqmgrdb_url = "%s/%s" % (data.couch_host, data.couch_reqmgr_db)
    wmdatamining.mcm_url = "https://cms-pdmv.cern.ch/mcm"
    wmdatamining.mcm_cert = "%s/auth/reqmgr2/dmwm-service-cert.pem" % ROOTDIR
    wmdatamining.mcm_key = "%s/auth/reqmgr2/dmwm-service-key.pem" % ROOTDIR
    wmdatamining.mcm_tmp_dir = "%s/state/reqmgr2/tmp" % __file__.rsplit('/', 4)[0]
    wmdatamining.wmdatamining_url = "%s/%s" % (data.couch_host, data.couch_wmdatamining_db)
    wmdatamining.activeDuration = 60 * 15  # every 15 mins
    wmdatamining.archiveDuration = 60 * 60 * 4 # every 4 hours
    
    # ACDC cleanup Thread
    couchCleanup = extentions.section_("couchCleanup")
    couchCleanup.object = "WMCore.ReqMgr.CherryPyThreads.CouchDBCleanup.CouchDBCleanup"
    couchCleanup.reqmgrdb_url = "https://cmsweb-testbed.cern.ch/couchdb/reqmgr_workload_cache"
    couchCleanup.acdc_url = "https://cmsweb-testbed.cern.ch/couchdb/acdcserver"
    couchCleanup.acdcCleanDuration = 60 * 60 * 4 # every 4 hours
