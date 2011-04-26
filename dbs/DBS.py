"""
DBS Server  configuration file
"""
import os,logging,sys
from WMCore.Configuration import Configuration
from WMCore.WMInit import getWMBASE

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]
DBSVERSION = 'DBS_3_0_8'

sys.path.append(os.path.join(ROOTDIR,'auth/dbs'))

from DBSSecrets import connectUrlReader
from DBSSecrets import databaseOwnerReader
from DBSSecrets import connectUrlWriter
from DBSSecrets import databaseOwnerWriter

config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = os.path.join(ROOTDIR,'auth/wmcore-auth/header-auth-key')

config.component_('Webtools')
config.Webtools.port = 8250
config.Webtools.log_screen = True
config.Webtools.proxy_base = 'True'
config.Webtools.application = 'dbs'

config.component_('dbs')
config.dbs.templates = os.path.join(getWMBASE(),'templates/WMCore/WebTools')
config.dbs.title = 'DBS Server'
config.dbs.description = 'CMS DBS Service'
config.dbs.section_('views')
config.dbs.admin = 'cmsdbs'
config.dbs.default_expires = 300

active = config.dbs.views.section_('active')
active.section_('DBSReader')
active.DBSReader.object = 'WMCore.WebTools.RESTApi'
active.DBSReader.section_('model')
active.DBSReader.model.object = 'dbs.web.DBSReaderModel'
active.DBSReader.section_('formatter')
active.DBSReader.formatter.object = 'WMCore.WebTools.RESTFormatter'

#Oracle
active.DBSReader.dbowner = databaseOwnerReader
active.DBSReader.version = DBSVERSION
active.DBSReader.section_('database')
active.DBSReader.database.connectUrl = connectUrlReader
active.DBSReader.database.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

active.section_('DBSWriter')
active.DBSWriter.object = 'WMCore.WebTools.RESTApi'
active.DBSWriter.section_('model')
active.DBSWriter.model.object = 'dbs.web.DBSWriterModel'
active.DBSWriter.section_('formatter')
active.DBSWriter.formatter.object = 'WMCore.WebTools.RESTFormatter'

#Oracle
active.DBSWriter.dbowner = databaseOwnerWriter
active.DBSWriter.version = DBSVERSION
active.DBSWriter.section_('database')
active.DBSWriter.database.connectUrl = connectUrlWriter
active.DBSWriter.database.engineParameters = { 'pool_size': 15, 'max_overflow': 10, 'pool_timeout' : 200 }

active.section_('MIGRATE')
active.MIGRATE.object = 'WMCore.WebTools.RESTApi'
active.MIGRATE.section_('model')
active.MIGRATE.model.object = 'dbs.web.DBSMigrateModel'
active.MIGRATE.section_('formatter')
active.MIGRATE.formatter.object = 'WMCore.WebTools.RESTFormatter'
active.MIGRATE.section_('database')
active.MIGRATE.database.connectUrl = connectUrlWriter
active.MIGRATE.dbowner = databaseOwnerWriter
active.MIGRATE.version = DBSVERSION
active.MIGRATE.nthreads = 4
