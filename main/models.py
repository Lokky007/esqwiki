from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.
class ProjectTasks(models.Model):
    id_project_task = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=256)
    description = models.CharField(max_length=2048)
    complete_percentage = models.IntegerField()
    finished = models.BooleanField(default=0)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)
