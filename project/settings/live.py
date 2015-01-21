from project.settings.default import *
# LIVE SETTINGS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Make this unique, and don't share it with anybody.
import os
SECRET_KEY = os.environ['SECRET_KEY']

