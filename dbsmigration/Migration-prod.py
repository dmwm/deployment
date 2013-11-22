"""
DBS3 Migration Server Configuration
"""
import os
import sys
from WMCore.Configuration import Configuration

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]

sys.path.append(os.path.join(ROOTDIR,'auth/dbs'))

###global instance
from DBSSecrets import dbs3_pl1_r
from DBSSecrets import dbs3_dg_i2
from DBSSecrets import dbs3_ig_i2

###phys03 instance
from DBSSecrets import dbs3_pp3_r

###phys02 instance
from DBSSecrets import dbs3_pp2_r

###phys01 instance
from DBSSecrets import dbs3_pp1_r

db_mapping = {'prod/global': dbs3_pl1_r,
              'dev/global': dbs3_dg_i2,
              'int/global': dbs3_ig_i2,
              'prod/phys03': dbs3_pp3_r,
              'prod/phys02': dbs3_pp2_r,
              'prod/phys01': dbs3_pp1_r}

thread_mapping = {'prod/global': 1,
                  'dev/global': 1,
                  'int/global': 1,
                  'prod/phys03': 1,
                  'prod/phys02': 2,
                  'prod/phys01': 1}

def create_instance_config(db_instances, instance_name):
    db_config_section = db_instances.section_(instance_name)
    db_config_section.threads = thread_mapping[instance_name]
    db_config_section.dbowner = db_mapping[instance_name]['databaseOwner']
    db_config_section.connectUrl = db_mapping[instance_name]['connectUrl']['writer']
    db_config_section.engineParameters = {'pool_size': 15, 'max_overflow': 10, 'pool_timeout': 200}

config = Configuration()

config.component_('web')
config.web.host = "127.0.0.1"
config.web.port = 8251
config.web.log_screen = True
config.web.thread_pool = 10

config.component_('dbsmigration')
config.dbsmigration.instances = ['prod/global', 'dev/global', 'int/global',
                                 'prod/phys03', 'prod/phys02', 'prod/phys01']
config.dbsmigration.section_('database')
db_instances = config.dbsmigration.database.section_('instances')

for instance_name in config.dbsmigration.instances:
    create_instance_config(db_instances, instance_name)
