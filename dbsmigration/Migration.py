"""
DBS3 Migration Server Configuration
"""
import os, sys, json
from WMCore.Configuration import Configuration

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]
TOPDIR = ROOTDIR.rsplit('/', 1)[0]
VARIANT="@@VARIANT@@"

# load secrets
sys.path.append(os.path.join(ROOTDIR, 'auth/dbs'))
from DBSSecrets import *

# get viewnames -> instance names list
with open(os.path.join(TOPDIR, 'state/dbsmigration/view_instances.json'), 'r') as f:
  view_mapping = json.load(f)

# instance name : connecturls, {reader needed roles, writer needed roles}
if VARIANT == 'prod':
  db_mapping = {'prod/global': dbs3_pg_r,
                'prod/phys01': dbs3_pp1_r,
                'prod/phys02': dbs3_pp2_r,
                'prod/phys03': dbs3_pp3_r,
                'prod/caf'   : dbs3_pc_r,
                'prod/test'  : dbs3_pt_i2}
elif VARIANT == 'preprod':
  db_mapping = {'int/global': dbs3_ig_i2,
                'int/phys01': dbs3_ip1_i2,
                'int/phys02': dbs3_ip2_i2,
                'int/phys03': dbs3_ip3_i2}
elif VARIANT == 'dev':
  db_mapping = {'dev/global': dbs3_dg_i2,
                'dev/phys01': dbs3_dp1_i2,
                'dev/phys02': dbs3_dp2_i2,
                'dev/phys03': dbs3_dp3_i2}
else:
  db_mapping = {'dev/global': dbs3_none_i2,
                'dev/phys03': dbs3_none_i2}

thread_mapping = {'prod/global': 1,
                  'prod/phys01': 1,
                  'prod/phys02': 1,
                  'prod/phys03': 1,
                  'prod/caf'   : 1,
                  'prod/test'  : 1,
                  'int/global' : 1,
                  'int/phys01' : 1,
                  'int/phys02' : 1,
                  'int/phys03' : 1,
                  'dev/global' : 1,
                  'dev/phys01' : 1,
                  'dev/phys02' : 1,
                  'dev/phys03' : 1}

config = Configuration()

config.component_('web')
config.web.host = "127.0.0.1"
config.web.port = 8251
config.web.log_screen = True
config.web.thread_pool = 50

config.component_('dbsmigration')
config.dbsmigration.instances = view_mapping[VARIANT]['DBSMigrate']
config.dbsmigration.section_('database')
db_instances = config.dbsmigration.database.section_('instances')
for instance_name in config.dbsmigration.instances:
  db_config_section = db_instances.section_(instance_name)
  db_config_section.threads = thread_mapping[instance_name]
  db_config_section.dbowner = db_mapping[instance_name]['databaseOwner']
  db_config_section.connectUrl = db_mapping[instance_name]['connectUrl']['writer']
  db_config_section.engineParameters = {'pool_size': 15, 'max_overflow': 10, 'pool_timeout': 200}
