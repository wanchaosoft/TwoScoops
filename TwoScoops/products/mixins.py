#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'TwoScoops'
__author__ = 'wanchao'
__create_time__ = '2018/1/2 16:34'

"""
from django.contrib import messages


class FlavorActionMixin(object):
    """Custom Form messages."""
    fields = ('title', 'slug', 'scoops_remaining')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)

