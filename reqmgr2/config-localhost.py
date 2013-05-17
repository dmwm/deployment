"""
deployment repository ReqMgr configuration file for localhost.

Running ReqMgr2:
run with absolute paths (DIR), problems e.g. creating PID file otherwise
cd WMCore
source ./setup.sh
# repeated running restarts the server
# state is work directory
bin/wmc-httpd -r -d DIR -l DIR/reqmgr.log ../deployment/reqmgr2/config-localhost.py

"""


import os

# load main production ReqMgr2 configuration file
deployment_dir = __file__.rsplit('/', 1)[0]
execfile(os.path.join(deployment_dir, "config.py"))

# localhost running additions, no authentication
config.main.section_("tools")
config.main.tools.section_("cms_auth")
config.main.server.socket_host = "127.0.0.1"
config.main.server.environment = "staging" # must not be "production"
config.main.tools.cms_auth.policy = "dangerously_insecure"

# go up /deployment/reqmgr2/__file__
first_part = os.path.abspath(__file__.rsplit('/', 3)[0])
config.views.ui.static_content_dir = os.path.join(first_part, "WMCore/src/data")

config.views.restapihub.couch_host = os.getenv("COUCHURL", None)
