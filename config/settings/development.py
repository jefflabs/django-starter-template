from .base import *

# Email backend for testing
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Media and static URLS
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, '../', "mediafiles")

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, '../', "staticfiles")