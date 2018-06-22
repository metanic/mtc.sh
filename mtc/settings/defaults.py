import os
import urllib


def env_value(name, default=None):
    name = name.upper()
    return os.environ.get('MTCSH_' + name, os.environ.get(name, default))


def project_path(*paths):
    return os.path.join(os.getcwd(), *paths)


def cache_url(url):
    parsed_url = urllib.parse.urlparse(url)
    location = parsed_url.hostname + ':' + str(parsed_url.port)

    return {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': location,
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': parsed_url.password,
        },
    }

ALLOWED_HOSTS = ['mtc.sh']
DATE_FORMAT = 'Y-m-d'
DEBUG = False
INTERNAL_IPS = []
MAILGUN_API_KEY = env_value('mailgun_api_key')
ROOT_URLCONF = 'mtc.core.urls'
USE_L10N = True

ACCESS_CONTROL_ALLOW_HEADERS = [
  'Content-Type',
  'Accept',
  'Authentication',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'raven.contrib.django.raven_compat',

    'mtc.shorten',

    'mtc.rest',  # TODO: Make this an external library
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'metanic.core.context_processors.frontend_url',
            ],
        }
    },
]
