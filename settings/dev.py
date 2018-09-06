from .base import *

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]