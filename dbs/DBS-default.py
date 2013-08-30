"""
DBS Server default configuration file
"""
import os
import sys
from WMCore.Configuration import Configuration

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]
DBSVERSION = os.getenv('DBS3_VERSION')

sys.path.append(os.path.join(ROOTDIR, 'auth/dbs'))

###global instance
from DBSSecrets import dbs3_p1_i2

###phys03 instance
from DBSSecrets import dbs3_l_i2

db_mapping = {'dev/global': dbs3_p1_i2,
              'dev/phys03': dbs3_l_i2}

security_params = {'dev/global': {'reader': {},
                                  'writer': {}},
                   'dev/phys03': {'reader': {},
                                  'writer': {}}}


def create_model_section(active, model):
    active.section_(model)
    current_model = getattr(active, model)
    current_model.object = 'WMCore.WebTools.RESTApi'
    current_model.section_('model')
    current_model.model.object = 'dbs.web.%sModel' % model
    current_model.section_('formatter')
    current_model.formatter.object = 'WMCore.WebTools.RESTFormatter'
    current_model.section_('database')
    current_model.section_('security')

    return current_model.database.section_('instances'), current_model.security.section_('instances')


def create_instance_config(db_instances, security_instances, instance_name, access):
    db_config_section = db_instances.section_(instance_name)
    db_config_section.dbowner = db_mapping[instance_name]['databaseOwner']
    db_config_section.version = DBSVERSION
    db_config_section.connectUrl = db_mapping[instance_name]['connectUrl'][access]
    db_config_section.engineParameters = {'pool_size': 15, 'max_overflow': 10, 'pool_timeout': 200}

    security_config_section = security_instances.section_(instance_name)
    security_config_section.params = security_params[instance_name][access]


config = Configuration()
config.component_('SecurityModule')
config.SecurityModule.key_file = os.path.join(ROOTDIR, 'auth/wmcore-auth/header-auth-key')

config.component_('Webtools')
config.Webtools.port = 8250
config.Webtools.log_screen = False
config.Webtools.proxy_base = 'True'
config.Webtools.application = 'dbs'
config.Webtools.environment = 'production'

config.component_('dbs')
config.dbs.templates = os.path.join(ROOTDIR, 'apps/dbs/statics')
config.dbs.title = 'DBS Server'
config.dbs.description = 'CMS DBS Service'
config.dbs.section_('views')
config.dbs.admin = 'cmsdbs'
config.dbs.default_expires = 900
config.dbs.instances = ['dev/global',
                        'dev/phys03']

###DBSReader section
active = config.dbs.views.section_('active')
db_instances, security_instances = create_model_section(active, 'DBSReader')

##instances configs
for instance_name in config.dbs.instances:
    create_instance_config(db_instances, security_instances, instance_name, access='reader')

###DBSWriter section
db_instances, security_instances = create_model_section(active, 'DBSWriter')

##instances configs
for instance_name in config.dbs.instances:
    create_instance_config(db_instances, security_instances, instance_name, access='writer')

###DBSMigrate section
db_instances, security_instances = create_model_section(active, 'DBSMigrate')

##instances configs
for instance_name in config.dbs.instances:
    create_instance_config(db_instances, security_instances, instance_name, access='writer')