# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from core.managers import PublishedManager
from core.models import TimeStampModel


class FlavorReview(models.Model):
    """Ice Cream flavor"""
    review = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    scoops_remaining = models.IntegerField()
    # custom model Manager
    objects = models.Manager()
    pub_objects = PublishedManager()

    class Meta:
        abstract = False
        db_table = 'flavor_preview'


# ============================== Custom User: First =================================
class IceCreamStore(models.Model):
    """Ice Cream Store
    This will use setting.AUTH_USER_MODEL as OneToOneField,
    don't use get_user_model() as ForeignKey"""
    # owner = models.OneToOneField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    u"""Other condition: use django-authtools to custom your User."""

    class Meta:
        abstract = False
        db_table = 'ice_cream_store'


class TestModel(FlavorReview):
    publish_date = models.DateTimeField()

    class Meta:
        abstract = False
        db_table = 'test_model'


# ============================== Custom User: Second =================================
class KarmaUser(AbstractUser, TimeStampModel):
    """Use AbstractUser::
        from django.contrib.auth.models import AbstractUser

        Use this, Django still establish default table(auth_user,etc ),
        but you will use karma_user table.
        Check: `get_user_model()` => `<class 'products.models.KarmaUser'>`
    """

    karma = models.PositiveIntegerField(verbose_name=_('karma'),
                                        default=0,
                                        blank=True)

    class Meta:
        db_table = 'karma_user'

    """You could choose another approach: subclass AbstractBaseUser.
    This is for who don't like default field (for example: first_name, etc.).
    You can custom your User more freedom."""





