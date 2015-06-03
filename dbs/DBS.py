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
with open(os.path.join(TOPDIR, 'state/dbs/view_instances.json'), 'r') as f:
  view_mapping = json.load(f)

# instance name : connecturls, {reader needed roles, writer needed roles}
if VARIANT == 'prod':
  db_mapping = {'prod/global': [dbs3_pg_r, {'reader':{},'writer':{'dbs': 'operator', 'dataops': 'production-operator'}}],
                'prod/phys01': [dbs3_pp1_r, {'reader':{},'writer':{}}],
                'prod/phys02': [dbs3_pp2_r, {'reader':{},'writer':{}}],
                'prod/phys03': [dbs3_pp3_r, {'reader':{},'writer':{}}],
                'prod/caf':    [dbs3_pc_r, {'reader':{},'writer':{}}],
                'prod/test':   [dbs3_pt_i2, {'reader':{},'writer':{}}]}

elif VARIANT == 'preprod':
  db_mapping = {'int/global': [dbs3_ig_i2,  {'reader':{},'writer':{'dbs': 'operator', 'dataops': 'production-operator'}}],
                'int/phys01': [dbs3_ip1_i2, {'reader':{},'writer':{}}],
                'int/phys02': [dbs3_ip2_i2, {'reader':{},'writer':{}}],
                'int/phys03': [dbs3_ip3_i2,{'reader':{},'writer':{}}]}
elif VARIANT == 'dev':
  db_mapping = {'dev/global': [dbs3_dg_i2, {'reader':{},'writer':{'dbs': 'operator', 'dataops': 'production-operator'}}],
                'dev/phys01': [dbs3_dp1_i2, {'reader':{},'writer':{}}],
                'dev/phys02': [dbs3_dp2_i2, {'reader':{},'writer':{}}],
                'dev/phys03': [dbs3_dp3_i2, {'reader':{},'writer':{}}]}
else:
  db_mapping = {'dev/global': [dbs3_none_i2,{'reader':{},'writer':{}}],
                'dev/phys03': [dbs3_none_i2, {'reader':{},'writer':{}}]}

config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = os.path.join(ROOTDIR, 'auth/wmcore-auth/header-auth-key')

config.component_('Webtools')
config.Webtools.port = 8250
config.Webtools.thread_pool = 50
config.Webtools.log_screen = False
config.Webtools.proxy_base = 'True'
config.Webtools.application = 'dbs'
config.Webtools.environment = 'production'

config.component_('dbs')
config.dbs.templates = os.path.join(ROOTDIR, 'apps/dbs/statics')
config.dbs.title = 'DBS Server'
config.dbs.description = 'CMS DBS Service'
config.dbs.section_('views')
config.dbs.admin = 'cmsdbs'
config.dbs.default_expires = 900
config.dbs.instances = list(set([i for r in view_mapping[VARIANT].values() for i in r]))

### Create views for DBSReader, DBSWriter and DBSMigrate
active = config.dbs.views.section_('active')
for viewname, access in [('DBSReader','reader'),('DBSWriter','writer'),('DBSMigrate','writer')]:
  if view_mapping[VARIANT][viewname]:
    active.section_(viewname)
    view = getattr(active, viewname)
    view.object = 'WMCore.WebTools.RESTApi'
    view.section_('model')
    view.model.object = 'dbs.web.%sModel' % viewname
    view.section_('formatter')
    view.formatter.object = 'WMCore.WebTools.RESTFormatter'
    view.section_('database')
    view.section_('security')
    dbinst=view.database.section_('instances')
    secinst=view.security.section_('instances')
    for instance_name in config.dbs.instances:
      dbconf = dbinst.section_(instance_name)
      dbconf.dbowner = db_mapping[instance_name][0]['databaseOwner']
      dbconf.version = DBSVERSION
      dbconf.connectUrl = db_mapping[instance_name][0]['connectUrl'][access]
      dbconf.engineParameters = {'pool_size': 15, 'max_overflow': 10, 'pool_timeout': 200}
      seconf = secinst.section_(instance_name)
      if instance_name in view_mapping[VARIANT][viewname]:
        seconf.params = db_mapping[instance_name][1][access]
      else:
        seconf.params = {'disabled': 'disabled'}
