"""
DBS Server default configuration file
"""
import os,logging,sys
from WMCore.Configuration import Configuration

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]
DBSVERSION = os.getenv('DBS3_VERSION')

sys.path.append(os.path.join(ROOTDIR,'auth/dbs'))

from DBSSecrets import dbs3_pl1_r
from DBSSecrets import dbs3_dg_i2
from DBSSecrets import dbs3_ig_i2

config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = os.path.join(ROOTDIR,'auth/wmcore-auth/header-auth-key')

config.component_('Webtools')
config.Webtools.port = 8250
config.Webtools.log_screen = False
config.Webtools.proxy_base = 'True'
config.Webtools.application = 'dbs'
config.Webtools.environment = 'production'

config.component_('dbs')
config.dbs.templates = os.path.join(ROOTDIR,'apps/dbs/data/templates/WMCore/WebTools')
config.dbs.title = 'DBS Server'
config.dbs.description = 'CMS DBS Service'
config.dbs.section_('views')
config.dbs.admin = 'cmsdbs'
config.dbs.default_expires = 900
config.dbs.instances = ['prod/global','dev/global','int/global']

active = config.dbs.views.section_('active')
active.section_('DBSReader')
active.DBSReader.object = 'WMCore.WebTools.RESTApi'
active.DBSReader.section_('model')
active.DBSReader.model.object = 'dbs.web.DBSReaderModel'
active.DBSReader.section_('formatter')
active.DBSReader.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.DBSReader.section_('database')
db_instances = active.DBSReader.database.section_('instances')

db_production_global = db_instances.section_('prod/global')
db_production_global.dbowner = dbs3_pl1_r['databaseOwner']
db_production_global.version = DBSVERSION
db_production_global.connectUrl = dbs3_pl1_r['connectUrl']['reader']
db_production_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

db_development_global = db_instances.section_('dev/global')
db_development_global.dbowner = dbs3_dg_i2['databaseOwner']
db_development_global.version = DBSVERSION
db_development_global.connectUrl = dbs3_dg_i2['connectUrl']['reader']
db_development_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

db_integration_global = db_instances.section_('int/global')
db_integration_global.dbowner = dbs3_ig_i2['databaseOwner']
db_integration_global.version = DBSVERSION
db_integration_global.connectUrl = dbs3_ig_i2['connectUrl']['reader']
db_integration_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

active.section_('DBSWriter')
active.DBSWriter.object = 'WMCore.WebTools.RESTApi'
active.DBSWriter.section_('model')
active.DBSWriter.model.object = 'dbs.web.DBSWriterModel'
active.DBSWriter.section_('formatter')
active.DBSWriter.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.DBSWriter.section_('database')
db_instances = active.DBSWriter.database.section_('instances')

db_production_global = db_instances.section_('prod/global')
db_production_global.dbowner = dbs3_pl1_r['databaseOwner']
db_production_global.version = DBSVERSION
db_production_global.connectUrl = dbs3_pl1_r['connectUrl']['writer']
db_production_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

db_development_global = db_instances.section_('dev/global')
db_development_global.dbowner = dbs3_dg_i2['databaseOwner']
db_development_global.version = DBSVERSION
db_development_global.connectUrl = dbs3_dg_i2['connectUrl']['writer']
db_development_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

db_integration_global = db_instances.section_('int/global')
db_integration_global.dbowner = dbs3_ig_i2['databaseOwner']
db_integration_global.version = DBSVERSION
db_integration_global.connectUrl = dbs3_ig_i2['connectUrl']['writer']
db_integration_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

active.DBSWriter.section_('security')
security_instances = active.DBSWriter.security.section_('instances')
security_production_global = security_instances.section_('prod/global')
security_production_global.params = {}
security_development_global = security_instances.section_('dev/global')
security_development_global.params = {}
security_integration_global = security_instances.section_('int/global')
security_integration_global.params = {}

active.section_('DBSMigrate')
active.DBSMigrate.object = 'WMCore.WebTools.RESTApi'
active.DBSMigrate.section_('model')
active.DBSMigrate.model.object = 'dbs.web.DBSMigrateModel'
active.DBSMigrate.section_('formatter')
active.DBSMigrate.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.DBSMigrate.section_('database')
db_instances = active.DBSMigrate.database.section_('instances')

db_production_global = db_instances.section_('prod/global')
db_production_global.dbowner = dbs3_pl1_r['databaseOwner']
db_production_global.version = DBSVERSION
db_production_global.connectUrl = dbs3_pl1_r['connectUrl']['writer']
db_production_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

db_development_global = db_instances.section_('dev/global')
db_development_global.dbowner = dbs3_dg_i2['databaseOwner']
db_development_global.version = DBSVERSION
db_development_global.connectUrl = dbs3_dg_i2['connectUrl']['writer']
db_development_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

db_integration_global = db_instances.section_('int/global')
db_integration_global.dbowner = dbs3_ig_i2['databaseOwner']
db_integration_global.version = DBSVERSION
db_integration_global.connectUrl = dbs3_ig_i2['connectUrl']['writer']
db_integration_global.engineParameters = { 'pool_size' : 15, 'max_overflow' : 10, 'pool_timeout' : 200 }

active.DBSMigrate.section_('security')
security_instances = active.DBSMigrate.security.section_('instances')
security_production_global = security_instances.section_('prod/global')
security_production_global.params = {}
security_development_global = security_instances.section_('dev/global')
security_development_global.params = {}
security_integration_global = security_instances.section_('int/global')
security_integration_global.params = {}
