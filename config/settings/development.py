"""Development Django settings."""

import os
from .base import *

DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() in ("true", "1", "yes")

# Development-only fallback key so local dev and tests boot without hardcoded production secrets.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-local-dev-only-key-do-not-use-in-production-9f4e2a1c",
)

ALLOWED_HOSTS = ["*"] if DEBUG else ALLOWED_HOSTS  # noqa: F405

REST_FRAMEWORK = {
    **REST_FRAMEWORK,  # noqa: F405
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
}
