"""
WMArchive configuration file.
"""

import os
import socket
from WMCore.Configuration import Configuration

HOST = socket.gethostname().lower()
# ROOTDIR = __file__.rsplit('/', 3)[0]
ROOTDIR = os.getenv('WMA_STATIC_ROOT', os.getcwd())
config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "wmarchive"
main.port = 8247  # main application port it listens on
main.index = 'data' # Configuration requires index attribute
# Security configuration
#main.authz_defaults = {"role": None, "group": None, "site": None}
#sec = main.section_("tools").section_("cms_auth")
#sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application)
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS data operations WMArchive."
app.title = "CMS Request Manager (WMArchive)"

# define different views for our application
views = config.section_("views")
# web UI interface
ui = views.section_('web') # was section 'ui'
ui.object = 'WMArchive.Service.FrontPage.FrontPage'
ui.static = ROOTDIR

# REST interface
data = views.section_('data')
data.object = 'WMArchive.Service.RestApi.RestInterface'
# data.short_storage_uri = 'fileio:%s/storage' % ROOTDIR
#data.short_storage_uri = 'avroio:%s/storage/schema.avsc' % ROOTDIR
data.short_storage_uri = 'mongodb://localhost:8230'
data.long_storage_uri = 'sparkio:///cms/wmarchive/data/schema.avsc'
data.long_storage_thr = 1*30*24*60*60 # 1 month
data.specmap = os.path.join(ROOTDIR, 'maps/qlmap.txt')
data.wmauri = 'http://localhost:%s' % main.port
# yarn option will be passed to myspark string
# use empty string for no yarn or --yarn or --yarn-cluster strings
data.yarn = ''
