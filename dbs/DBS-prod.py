"""
DBS Server cmsweb prod configuration file
"""
import os,logging,sys
from WMCore.Configuration import Configuration
from WMCore.WMInit import getWMBASE

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]
DBSVERSION = os.getenv('DBS3_VERSION')

sys.path.append(os.path.join(ROOTDIR,'auth/dbs'))

from DBSSecrets import dbs3_l3_i2
from DBSSecrets import dbs3_p1_i2
from DBSSecrets import dbs3_l1_i2

config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = os.path.join(ROOTDIR,'auth/wmcore-auth/header-auth-key')

config.component_('Webtools')
config.Webtools.port = 8250
config.Webtools.log_screen = True
config.Webtools.proxy_base = 'True'
config.Webtools.application = 'dbs'
config.Webtools.environment = 'production'

config.component_('dbs')
config.dbs.templates = os.path.join(getWMBASE(),'../../templates/WMCore/WebTools')
config.dbs.title = 'DBS Server'
config.dbs.description = 'CMS DBS Service'
config.dbs.section_('views')
config.dbs.admin = 'cmsdbs'
config.dbs.default_expires = 300
config.dbs.instances = ['prod/global','dev/global','int/global']

active = config.dbs.views.section_('active')
active.section_('DBSReader')
active.DBSReader.object = 'WMCore.WebTools.RESTApi'
active.DBSReader.section_('model')
active.DBSReader.model.object = 'dbs.web.DBSReaderModel'
active.DBSReader.section_('formatter')
active.DBSReader.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.DBSReader.section_('database')
instances = active.DBSReader.database.section_('instances')

ProductionGlobal = instances.section_('prod/global')
ProductionGlobal.dbowner = dbs3_p1_i2['databaseOwner']
ProductionGlobal.version = DBSVERSION
ProductionGlobal.connectUrl = dbs3_p1_i2['connectUrl']['reader']
ProductionGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

DevelopmentGlobal = instances.section_('dev/global')
DevelopmentGlobal.dbowner = dbs3_l1_i2['databaseOwner']
DevelopmentGlobal.version = DBSVERSION
DevelopmentGlobal.connectUrl = dbs3_l1_i2['connectUrl']['reader']
DevelopmentGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

IntegrationGlobal = instances.section_('int/global')
IntegrationGlobal.dbowner = dbs3_l3_i2['databaseOwner']
IntegrationGlobal.version = DBSVERSION
IntegrationGlobal.connectUrl = dbs3_l3_i2['connectUrl']['reader']
IntegrationGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

active.section_('DBSWriter')
active.DBSWriter.object = 'WMCore.WebTools.RESTApi'
active.DBSWriter.section_('model')
active.DBSWriter.model.object = 'dbs.web.DBSWriterModel'
active.DBSWriter.section_('formatter')
active.DBSWriter.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.DBSWriter.section_('database')
instances = active.DBSWriter.database.section_('instances')

ProductionGlobal = instances.section_('prod/global')
ProductionGlobal.dbowner = dbs3_p1_i2['databaseOwner']
ProductionGlobal.version = DBSVERSION
ProductionGlobal.connectUrl = dbs3_p1_i2['connectUrl']['writer']
ProductionGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

DevelopmentGlobal = instances.section_('dev/global')
DevelopmentGlobal.dbowner = dbs3_l1_i2['databaseOwner']
DevelopmentGlobal.version = DBSVERSION
DevelopmentGlobal.connectUrl = dbs3_l1_i2['connectUrl']['writer']
DevelopmentGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

IntegrationGlobal = instances.section_('int/global')
IntegrationGlobal.dbowner = dbs3_l3_i2['databaseOwner']
IntegrationGlobal.version = DBSVERSION
IntegrationGlobal.connectUrl = dbs3_l3_i2['connectUrl']['writer']
IntegrationGlobal.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }
