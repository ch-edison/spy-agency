from .base import *
from .base import env
import os
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-e7l1s@s&b@id5(qfs$4@#_wc*hs&u@#0qpkauofg3k*5n&h^n2",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

STATIC_URL = 'staticfiles/'
STATIC_ROOT = str(BASE_DIR / 'staticfiles')
STATICFILES_DIRS = []

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]
CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']