from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.
class AccessRight(models.Model):
    id_access_right = models.AutoField(primary_key=True)
    access_name = models.CharField(blank=False, null=False, max_length=256)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)


class CategoryBlock(models.Model):
    id_category_block = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=256)
    text = models.CharField(blank=False, null=False, max_length=2048)
    show = models.BooleanField(default=True)
    access_right = models.ForeignKey(AccessRight, blank=True, null=True)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=False, max_length=256)
    description = models.CharField(max_length=2048)
    show = models.BooleanField(default=True)
    access_right = models.ForeignKey(AccessRight, blank=True, null=True)
    id_category_block = models.ForeignKey(CategoryBlock, blank=True, null=True)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Topic(models.Model):
    id_topic = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=256)
    text = models.CharField(blank=False, null=False, max_length=2048)
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, blank=True, null=True)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)

    @property
    def count_answers(self):
        return Answer.objects.filter(topic_id=self.id_topic, deleted=0).count()

    @property
    def last_answers_data(self):
        if Answer.objects.filter(topic_id=self.id_topic, deleted=0).exists():
            return Answer.objects.filter(topic_id=self.id_topic, deleted=0).order_by('-x_created')[0]
        return None;


class Answer(models.Model):
    id_answer = models.AutoField(primary_key=True)
    text = models.CharField(blank=False, null=False, max_length=2048)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    topic = models.ForeignKey(Topic)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)



