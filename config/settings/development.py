from .base import *

# Email backend for testing
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Media and static file URLS
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),  # Add your project's static directory here
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Where static files are collected

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
