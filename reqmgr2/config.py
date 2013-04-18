"""
ReqMgr only configuration file.
Everything configurable in ReqMgr is defined here.

Running the ReqMgr service:
    - run always with absolute paths, problems e.g. creating PID file otherwise
        (relative paths did have issues when running multiple services)
    - work directory passed to wmc-httpd script
    - the command below can either be run on localhost manually
        with deployment/reqmgr2/config-localhost.py passed or is run on VM
        from the application manage script
    bin/wmc-httpd -r -d state_dir -l log_dir/reqmgr.log DEPLOYMENT/reqmgr2/config.py
    
"""

import re
import socket

from WMCore.Configuration import Configuration

# on localhost, this value is later set in config-localhost.py
# on VM and CMS web deployments, this value is set from the deploy
# script. Do not fill in anything manually here.
# The motivation is to have all vocms machine references at 1 place
# which is in the deploy script
COUCH_HOST = "COUCH_HOST_VALUE_PLACEHOLDER"


config = Configuration()
 
main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
# this is a bit shady, since this name is later in WMCore.REST.Main
# cfg.main.application.lower() L:491 and has to agree with 
# app = config.section_("reqmgr2"), otherwise configuration validation fails
main.application = "reqmgr2"
# main application port it listens on
main.port = 8246
main.index = "resthub"

# TODO/NOTE:
# defined in the ReqMgr1 configuration, HTTPFrontEnd/RequestManager/ReqMgrConfiguration.py
# probably not necessary, to be fetched from SiteDB
# config.reqmgr.security_roles = ['Admin', 'Developer', 'Data Manager', 'developer', 'admin', 'data-manager']        
main.authz_defaults = {"role": None, "group": None, "site": None}
sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application) # string containing "reqmgr2"
#app.admin = "cms-service-webtools@cern.ch"
app.admin = "zdenek.maxa@cern.ch"
app.description = "CMS data operations Request Manager."
app.title = "CMS Request Manager (ReqMgr)"        

views = config.section_("views")

# redirector for the REST API implemented handlers
resthub = views.section_("resthub")
resthub.object = "WMCore.ReqMgr.service.hub.Hub"
resthub.couch_host = COUCH_HOST
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
ui.static_content_dir = "/data/current/apps/%s/data" % main.application