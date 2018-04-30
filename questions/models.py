from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class questions(models.Model):
    id_question_post = models.AutoField(primary_key =True)
    id_question_post_parent = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=2048)
    deleted = models.BooleanField(default=0)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)


