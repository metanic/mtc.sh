import dj_database_url

from mtc.settings.defaults import *  # noqa

ALLOWED_HOSTS = [
    'mtc.sh',
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