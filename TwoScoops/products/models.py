from django.db import models
from django.utils import timezone

# Create your models here.
from core.managers import PublishedManager


class FlavorReview(models.Model):
    """Ice Cream flavor"""
    review = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    # custom model Manager
    objects = PublishedManager()
