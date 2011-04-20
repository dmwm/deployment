from WMCore.Configuration import Configuration
from WMCore.WMBase import getWMBASE
import os.path
from os import environ

config = Configuration()

# This component has all the configuration of CherryPy
config.component_('Webtools')

# This is the application
config.Webtools.port = 8201
# INADDR_ANY: listen on all interfaces (be visible outside of localhost)
config.Webtools.host = '0.0.0.0'
config.Webtools.application = 'FileMover'

# This is the config for the application
config.component_('FileMover')

# Define the default location for templates for the app
config.FileMover.templates = environ['FILEMOVER_ROOT'] + '/lib/python2.6/site-packages/fm/web/templates'
config.FileMover.admin = 'cms-service-webtools@cern.ch'
config.FileMover.title = 'CMS FileMover Documentation'
config.FileMover.description = 'Documentation on the FileMover'
config.FileMover.index = "FileMover"

# dbs section
dbs = config.FileMover.section_('dbs')
dbs.url = 'http://cmsdbsprod.cern.ch'
dbs.instance = 'cms_dbs_prod_global'
dbs.params = {'apiversion': 'DBS_2_0_9', 'api': 'executeQuery'}

# Views are all pages
config.FileMover.section_('views')

# These are all the active pages that Root.py should instantiate
active = config.FileMover.views.section_('active')

active.section_('FileMover')
active.FileMover.object = 'fm.web.FileMoverService'

# FileMover WebServer configuration
fmws = config.FileMover.section_('fmws')
fmws.day_transfer = 10
fmws.verbose = 1
fmws.max_transfer = 3
fmws.logger_dir = __file__.rsplit('/', 1)[0]
fmws.download_area = '%s/state/filemover/download' % __file__.rsplit('/', 4)[0]

# FileManager configuration
file_manager = config.FileMover.section_('file_manager')
file_manager.base_directory = '%s/state/filemover' % __file__.rsplit('/', 4)[0]
file_manager.max_size_gb = 20
file_manager.max_movers = 5

# FileLookup configuration
file_lookup = config.FileMover.section_('file_lookup')
file_lookup.priority_2 = 'T1'
file_lookup.priority_1 = 'T2'
file_lookup.priority_0 = 'T1_US'

# Transfer wrapper command configuration
transfer_wrapper = config.FileMover.section_('transfer_wrapper')
transfer_wrapper.transfer_command = 'srmcp -debug=true -srm_protocol_version=2 -retry_num=1 -streams_num=1'

# Security module stuff
config.component_('SecurityModule')
config.SecurityModule.key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]
