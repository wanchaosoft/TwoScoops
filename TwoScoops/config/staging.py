#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
......
"""

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'stagdb.sqlite3'),
    }
}



