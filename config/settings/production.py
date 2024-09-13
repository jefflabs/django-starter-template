from .base import *

# Email backend for production -> NOTE: you need a mailgun account and add EMAIL_USER and EMAIL_PASSWORD to .env file
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_USE_TLS = True

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
