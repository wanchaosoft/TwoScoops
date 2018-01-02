from django.db import models
from django.utils import timezone

# Create your models here.
from core.managers import PublishedManager


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


class TestModel(FlavorReview):
    publish_date = models.DateTimeField()

    class Meta:
        abstract = False


