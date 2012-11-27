from SiteDB.Config import Config
import os, socket

os.environ["NLS_LANG"] = ".AL32UTF8"

THREADS = 50
HOST = socket.gethostname().lower()
KEY_FILE = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
config = Config(nthreads = THREADS, authkey = KEY_FILE)

if HOST.startswith("vocms127"):
  config.views.data.ldapsync = True
  config.views.data.ldsyncto = "dev"
  config.views.data.ldsynctime = 300

# config.main.tools.cms_auth.policy = 'dangerously_insecure'
# config.main.server.environment = 'staging'
# config.main.server.socket_host = '127.0.0.1'

# config.main.profile = True
# config.main.instrument = 'igprof -d -pp -z --'
# config.main.instrument = 'valgrind'
