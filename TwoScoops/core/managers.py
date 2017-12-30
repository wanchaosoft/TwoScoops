#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'TwoScoops'
__author__ = 'wanchao'
__create_time__ = '2017/12/30 17:56'

"""
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    """pub_date Manager"""
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(pub_date__lte=timezone.now(), **kwargs)


