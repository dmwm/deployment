from confSettings import confSettings
import os, sys

sys.path.append('/data/srv/current/auth/popdbweb')
from djangokey import SECRET_KEY

popsettings = confSettings()
# Django settings for popDBDjango project.

os.environ['PYTHON_EGG_CACHE'] = popsettings.getSetting("popularity_project", "base_dir") + '/cache'

DEBUG = False
if popsettings.getSetting("popularity_project", "debug_mode") == "True":
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

APPEND_SLASH = False

DATABASES = popsettings.getNestedConfigSectionMap('db_sections')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = popsettings.getSetting("popularity_project", "static_dir")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/popdb/media/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
# Taken from the victor_djangokey.py secrets file
#SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

"""
to enable cache feature add
'django.middleware.cache.UpdateCacheMiddleware',
'django.middleware.cache.FetchFromCacheMiddleware',
as first and last middleware class 
"""
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    popsettings.getSetting("popCommon", "TEMPLATE_DIR"),
    popsettings.getSetting("popularity", "TEMPLATE_DIR"),
    popsettings.getSetting("victorinterface", "TEMPLATE_DIR"),
    popsettings.getSetting("xrdPopularity", "TEMPLATE_DIR"),

    #"/home/dboard/projectDjangoMerge/Popularity/templates",

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.contrib.messages.context_processors.messages",
)

ALLOWED_INCLUDE_ROOTS = (
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'Apps.popCommon',
    'Apps.popularity',
    'Apps.victorinterface',
    'Apps.xrdPopularity',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s -- %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            }
        },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },

        'log_file_popularity': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "%s/%s" % (popsettings.getSetting("popularity_project", "LOG_DIR"), "popularity_log"),
            'maxBytes': 1024*1024*5, # 5MB
            'backupCount': 10,
            'formatter': 'verbose'
        },

        'log_file_victorinterface': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "%s/%s" % (popsettings.getSetting("popularity_project", "LOG_DIR"), "victorinterface_log"),
            'maxBytes': 1024*1024*5, # 5MB
            'backupCount': 10,
            'formatter': 'verbose'
        },

        'log_file_xrdPopularity': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "%s/%s" % (popsettings.getSetting("popularity_project", "LOG_DIR"), "xrdPopularity_log"),
            'maxBytes': 1024*1024*5, # 5MB
            'backupCount': 10,
            'formatter': 'verbose'
        },


        'log_file_popCommon': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "%s/%s" % (popsettings.getSetting("popularity_project", "LOG_DIR"), "popCommon_log"),
            'maxBytes': 1024*1024*5, # 5MB
            'backupCount': 10,
            'formatter': 'verbose'
        },

    },

    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

        'Apps.popularity': {
            'handlers': ['log_file_popularity'],
            'level': 'INFO',
            'propagate': False,
        },

        'Apps.victorinterface': {
            'handlers': ['log_file_victorinterface'],
            'level': 'INFO',
            'propagate': False,
        },

        'Apps.xrdPopularity': {
            'handlers': ['log_file_xrdPopularity'],
            'level': 'INFO',
            'propagate': False,
        },


        'Apps.popCommon': {
            'handlers': ['log_file_popCommon'],
            'level': 'INFO',
            'propagate': False,
        }

    }
}
