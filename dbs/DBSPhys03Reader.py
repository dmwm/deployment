"""
DBS Server configuration file
"""
import os, sys, json
from WMCore.Configuration import Configuration

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]
TOPDIR = ROOTDIR.rsplit('/', 1)[0]
DBSVERSION = os.getenv('DBS3_VERSION')
VARIANT="@@VARIANT@@"

# load secrets
sys.path.append(os.path.join(ROOTDIR, 'auth/dbs'))
from DBSSecrets import *

# get viewnames -> instance names list
with open(os.path.join(TOPDIR, 'state/dbs/view_instances_p3r.json'), 'r') as f:
  view_mapping = json.load(f)

# instance name : connecturls, {reader needed roles, writer needed roles}
if VARIANT == 'prod':
  db_mapping = {'prod/phys03': [dbs3_pp3_r, {'reader':{},'writer':{}}]}
elif VARIANT == 'preprod':
  db_mapping = {'int/phys03': [dbs3_ip3_i2,{'reader':{},'writer':{}}]}
elif VARIANT == 'dev':
  db_mapping = {'dev/phys03': [dbs3_dp3_i2, {'reader':{},'writer':{}}]}
elif VARIANT == 'k8s':
  db_mapping = {'int/phys03': [dbs3_k8sp_r, {'reader':{},'writer':{}}]}
elif VARIANT == 'k8s-dev':
  db_mapping = {'dev/phys03': [dbs3_p2_i2,{'reader':{},'writer':{}}]}
else:
  db_mapping = {'dev/phys03': [dbs3_p_i2, {'reader':{},'writer':{}}]}

config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = os.path.join(ROOTDIR, 'auth/wmcore-auth/header-auth-key')

config.component_('Webtools')
config.Webtools.port = 8254
config.Webtools.thread_pool = 15
# The maximum number of requests which will be queued up before
# the server refuses to accept it (default -1, meaning no limit).
config.Webtools.accepted_queue_size = -1
config.Webtools.accepted_queue_timeout = 5
# enable CherryPy statistics monitoring
config.Webtools.cpstats = True
config.Webtools.log_screen = False
config.Webtools.proxy_base = 'True'
config.Webtools.application = 'dbspy'
config.Webtools.environment = 'production'

config.component_('dbspy')
config.dbspy.templates = os.path.join(ROOTDIR, 'apps/dbs/statics')
config.dbspy.title = 'DBS Server'
config.dbspy.description = 'CMS DBS Service'
config.dbspy.section_('views')
config.dbspy.admin = 'cmsdbs'
config.dbspy.default_expires = 900
config.dbspy.instances = view_mapping[VARIANT]["DBSReader"]

### Create views for DBSReader, DBSWriter and DBSMigrate
active = config.dbspy.views.section_('active')
for viewname, access in [('DBSReader','reader')]:
  if view_mapping[VARIANT][viewname]:
    active.section_(viewname)
    view = getattr(active, viewname)
    view.object = 'WMCore.WebTools.RESTApi'
    view.section_('model')
    view.model.object = 'dbs.web.%sModel' % viewname
    view.section_('formatter')
    view.formatter.object = 'WMCore.WebTools.DBSRESTFormatter'
    view.section_('database')
    view.section_('security')
    dbinst=view.database.section_('instances')
    secinst=view.security.section_('instances')
    for instance_name in config.dbspy.instances:
      dbconf = dbinst.section_(instance_name)
      dbconf.throllting_limit = 15
      #dbconf.throllting_time = 1
      dbconf.dbowner = db_mapping[instance_name][0]['databaseOwner']
      dbconf.version = DBSVERSION
      dbconf.connectUrl = db_mapping[instance_name][0]['connectUrl'][access]
      dbconf.engineParameters = {'pool_size': 15, 'max_overflow': 10, 'pool_timeout': 200}
      seconf = secinst.section_(instance_name)
      if instance_name in view_mapping[VARIANT][viewname]:
        seconf.params = db_mapping[instance_name][1][access]
      else:
        seconf.params = {'disabled': 'disabled'}
