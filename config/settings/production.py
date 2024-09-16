from .base import *

# Email backend (e.g. for onboarding flow) for production -> NOTE: you need a mailgun account and add EMAIL_USER and EMAIL_PASSWORD to .env file
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_USE_TLS = True

# onboarding settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True

# Media and static file URLS
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, '../', "mediafiles")

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, '../', "staticfiles")

# Caching -> using Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.cache.RedisCache",
        "LOCATION": config("REDIS_BACKEND"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CACHE_DURATION = 60 * 60 *24 * 7  # Cache for 7 days in seconds -> used for country list and detail pages


# Database
# Replaced the standard sqlite backend for a postgresql -> postgis database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        # TODO: "ENGINE": "django.contrib.gis.db.backends.postgis",
        "ENGINE": "django.db.backends.postgresql",
        'HOST': config("DB_HOSTNAME"),
        "NAME": config("DB_NAME"),
        "PORT": config("DB_PORT", cast=int),
        "USER": config("DB_USERNAME"),
        "PASSWORD": config("DB_PASSWORD"),
        'CONN_MAX_AGE': 600,  # Keep connections open for 10 minutes
    }
}
