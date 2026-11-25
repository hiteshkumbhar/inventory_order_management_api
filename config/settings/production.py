"""Production Django settings with strict security enforcement."""

import os
from django.core.exceptions import ImproperlyConfigured
from .base import *  # noqa: F403

DEBUG = False

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")

if not SECRET_KEY or SECRET_KEY.startswith("replace-with"):
    raise ImproperlyConfigured(
        "DJANGO_SECRET_KEY environment variable must be set to a secure secret in production."
    )

if not DATABASES["default"].get("PASSWORD"):  # noqa: F405
    raise ImproperlyConfigured("POSTGRES_PASSWORD environment variable must be set in production.")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "True").lower() in ("true", "1")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", "31536000"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
