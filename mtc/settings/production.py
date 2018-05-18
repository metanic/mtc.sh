import dj_database_url

from mtc.settings.defaults import *  # noqa

SECRET_KEY = env_value('SECRET_KEY')

ALLOWED_HOSTS = [
    'mtc.sh',
    'mtcsh.herokuapp.com',
]

CACHES = {
    'default': cache_url(env_value('redis_url')),
}

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
}

RAVEN_CONFIG = {
    'dsn': env_value('sentry_dsn'),
}
