import dj_database_url

from mtc.settings.defaults import *  # noqa

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

# Checks to ensure things aren't ridiculous
if len(SECRET_KEY) < 32:
    raise ValueError(
        "Please generate a longer secret key. Extra characters won't hurt. They'll "
        "only help. A 32 character minimum is required, but longer strings are better."
    )