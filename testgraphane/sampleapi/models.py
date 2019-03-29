import uuid
from django.db import models


class SampleObject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(default="Elo", max_length=20)
    description = models.TextField()


class ObjectsChild(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(default="Elo child", max_length=20)
    parent = models.ForeignKey(SampleObject, on_delete=models.CASCADE)
