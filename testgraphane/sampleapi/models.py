import uuid
from django.db import models


class SampleObject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(default="Elo", max_length=20)
    description = models.TextField()
