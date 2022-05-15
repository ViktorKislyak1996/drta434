from django.db import models
from django.db.models import JSONField


class Main(models.Model):
    title = models.CharField(max_length=100)
    data = JSONField()

    def __str__(self):
        return self.title
