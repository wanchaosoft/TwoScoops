from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    """An abstract Model that self-updating
    ``created`` and ``modified``fields."""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
