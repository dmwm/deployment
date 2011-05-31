#
# This is an example configuration which loads the documentation classes for
# the webtools package and shows you how to configure the various different
# classes available. Your application should have it's own configuration in it's
# CVS area and not use this, other than as a guideline. Applications deployed at
# CERN will need to meet the CERN web service SLA:
#     https://twiki.cern.ch/twiki/bin/view/CMS/DMWTServiceLevelAgreement
# This includes committing configuration files to appropriate locations in CVS.
#
from WMCore.Configuration import Configuration
from WMCore.WMBase import getWMBASE
import os.path,cherrypy
import os

PATH = os.path.abspath(os.path.dirname(__file__))

config = Configuration()

# This component has all the configuration of CherryPy
config.component_('Webtools')
# We could change port, set logging etc here like so:
config.Webtools.port = 8300
config.Webtools.host = '0.0.0.0'

config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

config.Webtools.application = 'T0Mon'

## This is the config for the application
config.component_('T0Mon')
## Define the default location for templates for the app
config.T0Mon.admin = ''
config.T0Mon.title = 'T0Mon'
config.T0Mon.description = 'Tier-0 Monitoring'
config.T0Mon.index = 'T0Mon'

## Views are all pages
config.T0Mon.section_('views')
## These are all the active pages that Root.py should instantiate
active = config.T0Mon.views.section_('active')

active.T0Mon = active.section_('T0Mon')
active.T0Mon.object = 'T0Mon.T0Mon'
active.T0Mon.templates = os.environ["T0MON_ROOT"] + '/lib/python2.6/site-packages/T0Mon/templates'
active.T0Mon.DAS='http://localhost:8304/tier0/'
active.T0Mon.plotfairy='http://vocms117.cern.ch:8351/plotfairy/'
active.T0Mon.emailAlert = 'gowdy@cern.ch'
