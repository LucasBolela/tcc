from django.db import models
from core.models import CreatedUpdated


class Tracker(CreatedUpdated):
    class Meta:
        db_table = "tracker"

    task = models.CharField(max_length=25, null=False, blank=False)
    success = models.BooleanField(default=True)
    response = models.JSONField(null=True)
