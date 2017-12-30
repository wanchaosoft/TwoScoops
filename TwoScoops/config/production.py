#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
settings for production

For Production Environment, Please set environment variable in os out of code.``SECRET_KEY``
"""
from django.core.exceptions import ImproperlyConfigured
from .base import *
import os


def get_env_variable(var_name):
    """Get the environment variable or return exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)
SECRET_KEY = get_env_variable("SECRET_KEY")

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'prodb.sqlite3'),
    }
}


