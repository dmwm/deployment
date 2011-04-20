from WMCore.Configuration import Configuration
from WMCore.WMBase import getWMBASE
import os.path

config = Configuration()
config.component_('Webtools')
config.Webtools.port = 8260
config.Webtools.host = '0.0.0.0'

# This is the application name
config.Webtools.application = "PlotFairy"

config.component_("PlotFairy")

#config.PlotFairy.index = 'plotfairy'
config.PlotFairy.admin = 'diego@cern.ch'
config.PlotFairy.title = 'CMS DMWM PlotFairy Service'
config.PlotFairy.description = 'The plot service for DMWM projects'


config.PlotFairy.section_('views')
active = config.PlotFairy.views.section_('active')

active.section_('plotfairy')
active.plotfairy.object = 'WMCore.WebTools.RESTApi'
active.plotfairy.templates = os.path.join(getWMBASE(), '/src/templates/WMCore/WebTools')

active.plotfairy.section_('database')
active.plotfairy.database.connectUrl = 'sqlite://'      # Dummy in memory SQLite DB
#active.plotfairy.database.engineParameters = {'pool_size': 10, 'max_overflow': 10, 'pool_timeout': 30}

active.plotfairy.section_('model')
active.plotfairy.model.object = 'WMCore.HTTPFrontEnd.PlotFairy.Plotter'

active.plotfairy.section_('formatter')
active.plotfairy.formatter.object = 'WMCore.HTTPFrontEnd.PlotFairy.PlotFormatter'

