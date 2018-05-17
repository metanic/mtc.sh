from mtc.settings.defaults import *  # noqa

DEBUG = True
SECRET_KEY = 'mtc.sh'
STATIC_URL = '/static/'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

DATABASES = {
    'default':
        {
            'ENGINE':
                'django.db.backends.sqlite3',
            'NAME':
                project_path(
                    env_value('DATABASE_FILENAME', 'metanic.sqlite3')
                ),
        },
}

INSTALLED_APPS += [
    'django_extensions',
]

INTERNAL_IPS = [
    '127.0.0.1',
]