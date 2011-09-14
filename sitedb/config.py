from SiteDB.Config import Config

THREADS = 30
KEY_FILE = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
config = Config(nthreads = THREADS, authkey = KEY_FILE)

# config.main.tools.cms_auth.policy = 'dangerously_insecure'
# config.main.server.environment = 'staging'
# config.main.server.socket_host = '127.0.0.1'

# config.main.profile = True
# config.main.instrument = 'igprof -d -pp -z --'
# config.main.instrument = 'valgrind'
