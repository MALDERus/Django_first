from django.db import models
from uuid import uuid4
# Create your models here.

class Books(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4())
    name = models.CharField(max_length=32)