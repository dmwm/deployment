from WMCore.Configuration import Configuration
from WMCore.WMBase import getWMBASE
import cherrypy

# Get the connection string
theFile = open( "../conf/t0datasvc/connect", "r" )
connectURL = theFile.read()
theFile.close()

###############################DAS
cherrypy.config.update({'environment': 'embedded'})
#cherrypy.config.update({'server.socket_host': 'vocms115'})
##########################################3
config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = "../conf/wmcore/header-auth-key"

config.component_('Webtools')
config.Webtools.port = 8304
config.Webtools.host = '0.0.0.0'
config.Webtools.application = 'Tier0Monitoring'
config.Webtools.expires=800
  # no caching as general policy, Mott0 has special rules defined in its service  source
config.component_('Tier0Monitoring')

config.Tier0Monitoring.templates = getWMBASE() + '/templates/WMCore/WebTools'
config.Tier0Monitoring.admin = 'gowdy@cern.ch'
config.Tier0Monitoring.title = 'T0DataSvc'
config.Tier0Monitoring.description = 'Tier-0 Data Service'


config.Tier0Monitoring.section_('views')
# These are all the active pages that Root.py should instantiate
active = config.Tier0Monitoring.views.section_('active')
tier0 = active.section_('tier0')
# The class to load for this view/page
tier0.object = 'WMCore.WebTools.RESTApi'
tier0.templates = getWMBASE() + '/templates/WMCore/WebTools/'
tier0.section_("database")
tier0.database.connectUrl = connectURL

#If you want to set up engineParameters take a look at
# http://www.sqlalchemy.org/docs/reference/sqlalchemy/connections.html
#tier0.database.engineParameters = {'pool_size': 10, 'max_overflow': 0}

tier0.section_('model')
tier0.model.object = 'T0.DAS.Tier0RESTModel'
tier0.section_('formatter')
tier0.formatter.object = 'WMCore.WebTools.DASRESTFormatter'
tier0.serviceModules = ['T0.DAS.Services.' + x for x in
                         ['MotT0Service','Tier0TomService','Tier0RECOService']]
