#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
test settings
"""

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'testdb.sqlite3'),
    }
}


