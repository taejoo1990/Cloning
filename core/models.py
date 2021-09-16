from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    # auto_now_add is to create now time when model is created
    created = models.DateTimeField(auto_now_add=True)
    # auto_now is to update now time when model is updated
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
