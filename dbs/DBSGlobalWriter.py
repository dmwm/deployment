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
# load NATS secrets and if it is not set make it available as None
try:
    from NATSSecrets import nats_secrets
except ImportError:
    nats_secrets = None
# load all other secrets
from DBSSecrets import *

# get viewnames -> instance names list
with open(os.path.join(TOPDIR, 'state/dbs/view_instances_gw.json'), 'r') as f:
  view_mapping = json.load(f)

# instance name : connecturls, {reader needed roles, writer needed roles}
if VARIANT == 'prod':
  db_mapping = {'prod/global': [dbs3_pg_r, {'reader':{},'writer':{'dbs': 'operator', 'dataops': 'production-operator'}}]}
elif VARIANT == 'preprod':
  db_mapping = {'int/global': [dbs3_ig_i2,  {'reader':{},'writer':{'dbs': 'operator', 'dataops': 'production-operator'}}]}
elif VARIANT == 'dev':
  db_mapping = {'dev/global': [dbs3_dg_i2, {'reader':{},'writer':{'dbs': 'operator', 'dataops': 'production-operator'}}]}
elif VARIANT == 'k8s':
  db_mapping = {'int/global': [dbs3_k8sg_r,{'reader':{},'writer':{'dbs': 'operator', 'dataops': 'production-operator'}}]}
elif VARIANT == 'k8s-dev':
  db_mapping = {'dev/global': [dbs3_p1_i2,{'reader':{},'writer':{}}]}
else:
  db_mapping = {'dev/global': [dbs3_l2_i2,{'reader':{},'writer':{}}]}
config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = os.path.join(ROOTDIR, 'auth/wmcore-auth/header-auth-key')

config.component_('Webtools')
config.Webtools.port = 8253
config.Webtools.thread_pool = 15
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
config.dbspy.instances = view_mapping[VARIANT]["DBSWriter"]

# NATS integration, nats_secrets will be supplied in DBSSecrets
if nats_secrets:
    config.dbspy.nats_server=nats_secrets
    config.dbspy.use_nats=True
    config.dbspy.nats_topics=[]

### Create views for DBSReader
active = config.dbspy.views.section_('active')
for viewname, access in [('DBSWriter','writer')]:
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
