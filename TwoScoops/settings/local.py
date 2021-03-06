#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
local settings of project for development
"""

from .base import *

AUTH_USER_MODEL = 'products.KarmaUser'  # app_label, model_name

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'devdb.sqlite3'),
        'ATOMIC_REQUESTS': True,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += ("debug_toolbar", )

MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']
