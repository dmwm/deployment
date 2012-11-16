from T0WmaDataSvc.Config import Config
import os, socket

os.environ["NLS_LANG"] = ".AL32UTF8"

THREADS = 10
HOST = socket.gethostname().lower()
KEY_FILE = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
config = Config(nthreads = THREADS, authkey = KEY_FILE)

# config.main.tools.cms_auth.policy = 'dangerously_insecure'
# config.main.server.environment = 'staging'
# config.main.server.socket_host = '127.0.0.1'
