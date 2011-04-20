from WMCore.Configuration import Configuration
from WMCore.WMBase import getWMBASE
import cherrypy

# Get the connection string
theFile = "%s/auth/t0datasvc/connect" % __file__.rsplit('/', 3)[0]
connectURL = open(theFile).read()

###############################DAS
cherrypy.config.update({'environment': 'embedded'})
#cherrypy.config.update({'server.socket_host': 'vocms115'})
##########################################3
config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

config.component_('Webtools')
config.Webtools.port = 8304
config.Webtools.host = '0.0.0.0'
config.Webtools.application = 'tier0'
config.Webtools.expires=800
  # no caching as general policy, Mott0 has special rules defined in its service  source
config.component_('tier0')

config.tier0.templates = getWMBASE() + '/templates/WMCore/WebTools'
config.tier0.admin = 'gowdy@cern.ch'
config.tier0.title = 'T0DataSvc'
config.tier0.description = 'Tier-0 Data Service'
config.tier0.index = 'tier0'


config.tier0.section_('views')
# These are all the active pages that Root.py should instantiate
active = config.tier0.views.section_('active')
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
