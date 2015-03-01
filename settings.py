# import os
# gettext = lambda s: s
#
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# DATA_DIR = os.path.dirname(os.path.dirname(__file__))
# # Django settings for egyptscholars project.
#
# DEBUG = True
# TEMPLATE_DEBUG = DEBUG
#
# ADMINS = (
#     # ('Your Name', 'your_email@example.com'),
# )
#
# MANAGERS = ADMINS
#
#
#
# # Hosts/domain names that are valid for this site; required if DEBUG is False
# # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = []
#
# # Local time zone for this installation. Choices can be found here:
# # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# # although not all choices may be available on all operating systems.
# # In a Windows environment this must be set to your system time zone.
# TIME_ZONE = 'UTC'
#
# # Language code for this installation. All choices can be found here:
# # http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en'
#
# SITE_ID = 1
#
# # If you set this to False, Django will make some optimizations so as not
# # to load the internationalization machinery.
# USE_I18N = True
#
# # If you set this to False, Django will not format dates, numbers and
# # calendars according to the current locale.
# USE_L10N = True
#
# # If you set this to False, Django will not use timezone-aware datetimes.
# USE_TZ = True
#
# # Absolute filesystem path to the directory that will hold user-uploaded files.
# # Example: "/var/www/example.com/media/"
# MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
#
# # URL that handles the media served from MEDIA_ROOT. Make sure to use a
# # trailing slash.
# # Examples: "http://example.com/media/", "http://media.example.com/"
# MEDIA_URL = '/media/'
#
# # Absolute path to the directory static files should be collected to.
# # Don't put anything in this directory yourself; store your static files
# # in apps' "static/" subdirectories and in STATICFILES_DIRS.
# # Example: "/var/www/example.com/static/"
# STATIC_ROOT = os.path.join(DATA_DIR, 'static')
#
# # URL prefix for static files.
# # Example: "http://example.com/static/", "http://static.example.com/"
# STATIC_URL = '/static/'
#
# # Additional locations of static files
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'egyptscholars', 'static'),
# )
#
#
# # List of finder classes that know how to find static files in
# # various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )
#
# # Make this unique, and don't share it with anybody.
# SECRET_KEY = 'f0&((4j*$0xk5^xa0mkf1&76c553^39glv%!oisk8#4)=3qrps'
#
# # List of callables that know how to import templates from various sources.
#
#
#
#
# ROOT_URLCONF = 'egyptscholars.urls'
#
# # Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'egyptscholars.wsgi.application'
#
#
#
#
#
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
#
# # A sample logging configuration. The only tangible logging
# # performed by this configuration is to send an email to
# # the site admins on every HTTP 500 error when DEBUG=False.
# # See http://docs.djangoproject.com/en/dev/topics/logging for
# # more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader'
# )
#
# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.locale.LocaleMiddleware',
#     'django.middleware.doc.XViewMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'cms.middleware.user.CurrentUserMiddleware',
#     'cms.middleware.page.CurrentPageMiddleware',
#     'cms.middleware.toolbar.ToolbarMiddleware',
#     'cms.middleware.language.LanguageCookieMiddleware',
#     'django.middleware.transaction.TransactionMiddleware'
# )
#
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.contrib.messages.context_processors.messages',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.request',
#     'django.core.context_processors.media',
#     'django.core.context_processors.csrf',
#     'django.core.context_processors.tz',
#     'sekizai.context_processors.sekizai',
#     'django.core.context_processors.static',
#     'cms.context_processors.cms_settings'
# )
#
# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'egyptscholars', 'templates'),
# )
#
# INSTALLED_APPS = (
#     'djangocms_admin_style',
#     'djangocms_text_ckeditor',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.admin',
#     'django.contrib.sites',
#     'django.contrib.sitemaps',
#     'django.contrib.staticfiles',
#     'django.contrib.messages',
#     'cms',
#     'menus',
#     'sekizai',
#     'mptt',
#     'djangocms_style',
#     'djangocms_column',
#     'djangocms_file',
#     'djangocms_flash',
#     'djangocms_googlemap',
#     'djangocms_inherit',
#     'djangocms_link',
#     'djangocms_picture',
#     'djangocms_teaser',
#     'djangocms_video',
#     'south',
#     'reversion',
#     'egyptscholars'
# )
#
# LANGUAGES = (
#     ## Customize this
#     ('en', gettext('en')),
# )
#
# CMS_LANGUAGES = {
#     ## Customize this
#     'default': {
#         'public': True,
#         'hide_untranslated': False,
#         'redirect_on_fallback': True,
#     },
#     1: [
#         {
#             'public': True,
#             'code': 'en',
#             'hide_untranslated': False,
#             'name': gettext('en'),
#             'redirect_on_fallback': True,
#         },
#     ],
# }
#
# CMS_TEMPLATES = (
#     ## Customize this
#     ('fullwidth.html', 'Fullwidth'),
#     ('sidebar_left.html', 'Sidebar Left'),
#     ('sidebar_right.html', 'Sidebar Right')
# )
#
# CMS_PERMISSION = True
#
# CMS_PLACEHOLDER_CONF = {}
#
# DATABASES = {
#     'default':
#         {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'project.db', 'HOST': 'localhost', 'USER': '', 'PASSWORD': '', 'PORT': ''}
# }

#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################

import os
gettext = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
# Django settings for egyptscholars project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('kemo', 'ahmedkamal19855@gmail.com'),
)

MANAGERS = ADMINS



# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
# USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'egyptscholars', 'static'),
# )


# List of finder classes that know how to find static files in
# various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h+q=ecz2ymj_b(^f@00#%xjde_=_s5%ub_6=13mpq+iji4$$uw'

# List of callables that know how to import templates from various sources.




# ROOT_URLCONF = 'egyptscholars.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'egyptscholars.wsgi.application'





# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader'
# )

# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.locale.LocaleMiddleware',
#     'django.middleware.doc.XViewMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'cms.middleware.user.CurrentUserMiddleware',
#     'cms.middleware.page.CurrentPageMiddleware',
#     'cms.middleware.toolbar.ToolbarMiddleware',
#     'cms.middleware.language.LanguageCookieMiddleware',
#     'django.middleware.transaction.TransactionMiddleware'
# )

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.contrib.messages.context_processors.messages',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.request',
#     'django.core.context_processors.media',
#     'django.core.context_processors.csrf',
#     'django.core.context_processors.tz',
#     'sekizai.context_processors.sekizai',
#     'django.core.context_processors.static',
#     'cms.context_processors.cms_settings'
# )

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'egyptscholars', 'templates'),
)

# INSTALLED_APPS = (
#     'djangocms_admin_style',
#     'djangocms_text_ckeditor',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.admin',
#     'django.contrib.sites',
#     'django.contrib.sitemaps',
#     'django.contrib.staticfiles',
#     'django.contrib.messages',
#     'cms',
#     'menus',
#     'sekizai',
#     'mptt',
#     'djangocms_style',
#     'djangocms_column',
#     'djangocms_file',
#     'djangocms_flash',
#     'djangocms_googlemap',
#     'djangocms_inherit',
#     'djangocms_link',
#     'djangocms_picture',
#     'djangocms_teaser',
#     'djangocms_video',
#     'south',
#     'reversion',
#     'egyptscholars'
# )

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    # ('slideshow.html', 'slideshow'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default':
        {'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'egyptscholars', 'HOST': '', 'USER': 'postgres', 'PASSWORD': '123', 'PORT': '5433'}
}

################################################  ASKBOT ################################################
################################################  ASKBOT ################################################
################################################  ASKBOT ################################################
################################################  ASKBOT ################################################
################################################  ASKBOT ################################################
################################################  ASKBOT ################################################
################################################  ASKBOT ################################################
################################################  ASKBOT ################################################

## Django settings for ASKBOT enabled project.
import os.path
import logging
import sys
import askbot
import site

#this line is added so that we can import pre-packaged askbot dependencies
ASKBOT_ROOT = os.path.abspath(os.path.dirname(askbot.__file__))
site.addsitedir(os.path.join(ASKBOT_ROOT, 'deps'))

DEBUG = True  # set to True to enable debugging
# TEMPLATE_DEBUG = False  # keep false when debugging jinja2 templates
INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ['*',]#change this for better security on your site

# ADMINS = (
#     ('Your Name', 'your_email@domain.com'),
# )

# MANAGERS = ADMINS

# DATABASE_ENGINE = 'postgresql_psycopg2' # only postgres (>8.3) and mysql are supported so far others have not been tested yet
# DATABASE_NAME = ''             # Or path to database file if using sqlite3.
# DATABASE_USER = ''             # Not used with sqlite3.
# DATABASE_PASSWORD = ''         # Not used with sqlite3.
# DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

#outgoing mail server settings
SERVER_EMAIL = ''
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = ''
EMAIL_HOST=''
EMAIL_PORT=''
EMAIL_USE_TLS=False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#incoming mail settings
#after filling out these settings - please
#go to the site's live settings and enable the feature
#"Email settings" -> "allow asking by email"
#
#   WARNING: command post_emailed_questions DELETES all
#            emails from the mailbox each time
#            do not use your personal mail box here!!!
#
IMAP_HOST = ''
IMAP_HOST_USER = ''
IMAP_HOST_PASSWORD = ''
IMAP_PORT = ''
IMAP_USE_TLS = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
# TIME_ZONE = 'America/Chicago'

# SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
# USE_I18N = True
# LANGUAGE_CODE = 'en'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'askbot', 'upfiles')
# MEDIA_URL = '/upfiles/'#url to uploaded media
# STATIC_URL = '/m/'#url to project static files

PROJECT_ROOT = os.path.dirname(__file__)
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')#path to files collected by collectstatic

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'#must be this value

# Make up some unique string, and don't share it with anybody.
# SECRET_KEY = 'sdljdfjkldsflsdjkhsjkldgjlsdgfs s '

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'askbot.skins.loaders.Loader',
    'django.template.loaders.eggs.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #below is askbot stuff for this tuple
    #'askbot.skins.loaders.load_template_source', #changed due to bug 97
    # 'askbot.skins.loaders.filesystem_load_template_source',
    #'django.template.loaders.eggs.load_template_source',
    # 'django.template.loaders.filesystem.Loader',
    # 'django.template.loaders.app_directories.Loader',

)


MIDDLEWARE_CLASSES = (
    #'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    ## Enable the following middleware if you want to enable
    ## language selection in the site settings.
    #'askbot.middleware.locale.LocaleMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.sqlprint.SqlPrintingMiddleware',

    #below is askbot stuff for this tuple
    'askbot.middleware.anon_user.ConnectToSessionMessagesMiddleware',
    'askbot.middleware.forum_mode.ForumModeMiddleware',
    'askbot.middleware.cancel.CancelActionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'askbot.middleware.view_log.ViewLogMiddleware',
    'askbot.middleware.spaceless.SpacelessMiddleware',

    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    # 'django.middleware.transaction.TransactionMiddleware'
)

JINJA2_EXTENSIONS = (
    'compressor.contrib.jinja2ext.CompressorExtension',
)

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)


ROOT_URLCONF = os.path.basename(os.path.dirname(__file__)) + '.urls'


#UPLOAD SETTINGS
FILE_UPLOAD_TEMP_DIR = os.path.join(
                                os.path.dirname(__file__),
                                'tmp'
                            ).replace('\\','/')

FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)
ASKBOT_ALLOWED_UPLOAD_FILE_TYPES = ('.jpg', '.jpeg', '.gif', '.bmp', '.png', '.tiff')
ASKBOT_MAX_UPLOAD_FILE_SIZE = 1024 * 1024 #result in bytes
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


#TEMPLATE_DIRS = (,) #template have no effect in askbot, use the variable below
#ASKBOT_EXTRA_SKINS_DIR = #path to your private skin collection
#take a look here http://askbot.org/en/question/207/

TEMPLATE_CONTEXT_PROCESSORS = (

    'django.contrib.auth.context_processors.auth', #this is required for admin
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    # 'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.tz',
    'django.core.context_processors.csrf', #necessary for csrf protection
    'django.core.context_processors.static',

    'askbot.context.application_settings',
    'askbot.user_messages.context_processors.user_messages',#must be before auth
    'askbot.deps.group_messaging.context.group_messaging_context',

    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings'
)

# ASKBOT_SELF_TEST = False
INSTALLED_APPS = (
    'longerusername',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'compressor',
    #'debug_toolbar',
    #'haystack',
    'askbot',
    'askbot.deps.django_authopenid',
    #'askbot.importers.stackexchange', #se loader
    'south',
    'askbot.deps.livesettings',
    'keyedcache',
    'robots',
    'django_countries',
    'djcelery',
    'djkombu',
    'followit',
    'tinymce',
    #'avatar',#experimental use git clone git://github.com/ericflo/django-avatar.git$

    'compressor',
    'group_messaging',
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'cms',
    'menus',
    'sekizai',
    'mptt',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'slideshow',
    'adminsortable',
    'easy_thumbnails',
    # 'south',
    'reversion',
    'egyptscholars'
)


#setup memcached for production use!
#see http://docs.djangoproject.com/en/1.1/topics/cache/ for details
CACHE_BACKEND = 'locmem://'
#needed for django-keyedcache
CACHE_TIMEOUT = 6000
#sets a special timeout for livesettings if you want to make them different
LIVESETTINGS_CACHE_TIMEOUT = CACHE_TIMEOUT
CACHE_PREFIX = 'askbot' #make this unique
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#If you use memcache you may want to uncomment the following line to enable memcached based sessions
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'askbot.deps.django_authopenid.backends.AuthBackend',
)

#logging settings
LOG_FILENAME = 'askbot.log'
logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), 'log', LOG_FILENAME),
    level=logging.CRITICAL,
    format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

###########################
#
#   this will allow running your forum with url like http://site.com/forum
#
#   ASKBOT_URL = 'forum/'
#
ASKBOT_URL = 'forum/' #no leading slash, default = '' empty string
ASKBOT_TRANSLATE_URL = True #translate specific URLs
_ = lambda v:v #fake translation function for the login url
LOGIN_URL = '/%s%s%s' % (ASKBOT_URL,_('account/'),_('signin/'))
LOGIN_REDIRECT_URL = ASKBOT_URL #adjust if needed
#note - it is important that upload dir url is NOT translated!!!
#also, this url must not have the leading slash
ALLOW_UNICODE_SLUGS = False
ASKBOT_USE_STACKEXCHANGE_URLS = False #mimic url scheme of stackexchange

#Celery Settings
BROKER_TRANSPORT = "djkombu.transport.DatabaseTransport"
CELERY_ALWAYS_EAGER = True

import djcelery
djcelery.setup_loader()

CSRF_COOKIE_NAME = 'askbot_csrf'
#enter domain name here - e.g. example.com
#CSRF_COOKIE_DOMAIN = ''

STATICFILES_DIRS = (
    ('default/media', os.path.join(ASKBOT_ROOT, 'media')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    # 'django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
##############################################################   disabled self test askbot

ASKBOT_SELF_TEST = False

##############################################################
RECAPTCHA_USE_SSL = True

#HAYSTACK_SETTINGS
ENABLE_HAYSTACK_SEARCH = False
#Uncomment for multilingual setup:
#HAYSTACK_ROUTERS = ['askbot.search.haystack.routers.LanguageRouter',]

#Uncomment if you use haystack
#More info in http://django-haystack.readthedocs.org/en/latest/settings.html
#HAYSTACK_CONNECTIONS = {
#            'default': {
#                        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#            }
#}

TINYMCE_COMPRESSOR = True
TINYMCE_SPELLCHECKER = False
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'default/media/js/tinymce/')

#TINYMCE_JS_URL = STATIC_URL + 'default/media/js/tinymce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'askbot_imageuploader,askbot_attachment',
    'convert_urls': False,
    'theme': 'advanced',
    'force_br_newlines': True,
    'force_p_newlines': False,
    'forced_root_block': '',
    'mode' : 'textareas',
    'oninit': "TinyMCE.onInitHook",
    'plugins': 'askbot_imageuploader,askbot_attachment',
    'theme_advanced_toolbar_location' : 'top',
    'theme_advanced_toolbar_align': 'left',
    'theme_advanced_buttons1': 'bold,italic,underline,|,bullist,numlist,|,undo,redo,|,link,unlink,askbot_imageuploader,askbot_attachment',
    'theme_advanced_buttons2': '',
    'theme_advanced_buttons3' : '',
    'theme_advanced_path': False,
    'theme_advanced_resizing': True,
    'theme_advanced_resize_horizontal': False,
    'theme_advanced_statusbar_location': 'bottom',
    'width': '730',
    'height': '250'
}

#delayed notifications, time in seconds, 15 mins by default
NOTIFICATION_DELAY_TIME = 60 * 15

GROUP_MESSAGING = {
    'BASE_URL_GETTER_FUNCTION': 'askbot.models.user_get_profile_url',
    'BASE_URL_PARAMS': {'section': 'messages', 'sort': 'inbox'}
}

ASKBOT_MULTILINGUAL = False

COMPRESS_JS_FILTERS = []
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
JINJA2_EXTENSIONS = ('compressor.contrib.jinja2ext.CompressorExtension',)

# Use syncdb for tests instead of South migrations. Without this, some tests
# fail spuriously in MySQL.
SOUTH_TESTS_MIGRATE = False

VERIFIER_EXPIRE_DAYS = 3
