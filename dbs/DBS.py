"""
DBS Server  configuration file
"""
import os, logging, os.path
from WMCore.Configuration import Configuration
import WMCore.WMInit

databaseOwner='fixme_database_account'

CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
LOGDIR = CONFIGDIR.rsplit('/', 1)[0] + "/logs"
# FIXME: goes too far out of DBS3 installation area?
# SWDIR = os.path.normcase(os.environ["DBS3_ROOT"]).rsplit('/', 3)[0]
# FIXME: needs real package dependency? why is this needed here?
# TEMPLATEDIR = os.path.join(SWDIR, '/cms/wmcore/WMAGENT_0_4_0-cmp/src/templates/WMCore/WebTools/')

print CONFIGDIR
# FIXME print SWDIR
print LOGDIR
# FIXME print TEMPLATEDIR

import pdb
pdb.set_trace()

DBSVersion = 'DBS_3_0_0'

config = Configuration()

#Agent section is required by WMCore
config.section_("Agent")
config.Agent.contact ="fixme_support_email_here@some.where"
#Only these two lines in "Agent" are required in order to turn off the default services.
config.Agent.useMsgService = False
config.Agent.useTrigger = False

config.section_("General")
config.General.workDir = os.environ['DBS3_ROOT']

#CoreDatabase section is required by WMCore.
config.section_("CoreDatabase")
# User specific parameter
config.CoreDatabase.version = DBSVersion
config.CoreDatabase.dbowner = databaseOwner
#Oracle
#config.CoreDatabase.connectUrl = 'oracle://fixme_database_account:fixme_password@fixme_instance'
config.CoreDatabase.connectUrl = 'oracle://fixme_database_account:fixme_password@fixme_instance'
config.CoreDatabase.engineParameters = {'pool_size': 15, 'max_overflow': 10, 'pool_timeout': 200 }

#config web server. These are required fields by WMCore althrough some of them are useless.
config.webapp_("cmsdbs")
config.cmsdbs.componentDir = LOGDIR+'/DBServer'
config.cmsdbs.server.host = "::"
config.cmsdbs.server.port = 8585
config.cmsdbs.templates = TEMPLATEDIR
config.cmsdbs.admin = "fixme_admin_email_needed_here@some.where"
config.cmsdbs.title = 'DBS Global Server'
config.cmsdbs.dbowner = databaseOwner
config.cmsdbs.description = 'CMS DBS Global Service'
config.cmsdbs.default_expires=300
#config.cmsdbs.index='DBSG'
config.cmsdbs.section_('views')
active=config.cmsdbs.views.section_('active')

#DBS server page/view
DBSG = active.section_('DBSG')
DBSG.object = 'WMCore.WebTools.RESTApi'
DBSG.section_('model')
DBSG.model.object = 'dbs.web.DBSWriterModel'
DBSG.section_('formatter')
active.DBSG.formatter.object = 'WMCore.WebTools.RESTFormatter'

#Migration server page/view
MIGRATEG = active.section_('MIGRATEG')
MIGRATEG.object = 'WMCore.WebTools.RESTApi'
MIGRATEG.section_('model')
MIGRATEG.model.object = 'dbs.web.DBSMigrateModel'
MIGRATEG.section_('formatter')
MIGRATEG.formatter.object = 'WMCore.WebTools.RESTFormatter'
MIGRATEG.version = DBSVersion
MIGRATEG.nthreads = 4

#config migration mover
config.component_('DBSMigrationMover')
config.DBSMigrationMover.default_expires=300
config.DBSMigrationMover.pollInterval = 1
config.DBSMigrationMover.namespace= "dbs.components.migration.DBSMigrationMover"
config.DBSMigrationMover.componentDir = LOGDIR + '/DBSGMigrationMover'
config.DBSMigrationMover.workerThreads = 1

#Config insert buffer
config.component_('DBSInsertBuffer')
config.DBSInsertBuffer.default_expires=300
config.DBSInsertBuffer.pollInterval = 1
config.DBSInsertBuffer.namespace= "dbs.components.insertbuffer.DBSInsertBuffer"
config.DBSInsertBuffer.componentDir = LOGDIR + '/DBSGInsertBuffer'
config.DBSInsertBuffer.workerThreads = 1
