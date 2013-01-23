"""
DBS3 Migration Server Configuration
"""
from WMCore.Configuration import Configuration
import os,sys

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]

sys.path.append(os.path.join(ROOTDIR,'auth/dbs'))

from DBSSecrets import dbs3_pl1_r
from DBSSecrets import dbs3_dg_i2
from DBSSecrets import dbs3_ig_i2

config = Configuration()

config.component_('web')
config.web.host = "127.0.0.1"
config.web.port = 8251
config.web.log_screen = True
config.web.thread_pool = 10

config.component_('dbsmigration')
config.dbsmigration.instances = ['prod/global','dev/global','int/global']
config.dbsmigration.section_('database')
db_instances = config.dbsmigration.database.section_('instances')

db_production_global = db_instances.section_('prod/global')
db_production_global.threads = 2
db_production_global.dbowner = dbs3_pl1_r['databaseOwner']
db_production_global.connectUrl = dbs3_pl1_r['connectUrl']['writer']
db_production_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

db_development_global = db_instances.section_('dev/global')
db_development_global.dbowner = dbs3_dg_i2['databaseOwner']
db_development_global.threads = 1
db_development_global.connectUrl = dbs3_dg_i2['connectUrl']['writer']
db_development_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

db_integration_global = db_instances.section_('int/global')
db_integration_global.threads = 1
db_integration_global.dbowner = dbs3_ig_i2['databaseOwner']
db_integration_global.connectUrl = dbs3_ig_i2['connectUrl']['writer']
db_integration_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }
