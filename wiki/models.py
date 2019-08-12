from __future__ import unicode_literals

from django.conf import settings
from django.db import models
import os


def get_image_path(instance, filename):
    return instance.id_wikiCraftProductType.name + "/" + filename


# Blacksmithy
class WikiCraftProductType(models.Model):
    id_wikiCraftProductType = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)



# Iron ore
class WikiItem(models.Model):
    id_wikiItem = models.AutoField(primary_key=True)
    id_map_coordinate = models.IntegerField(default=None, blank=True, null=True)
    id_wikiCraftProductType = models.ForeignKey(WikiCraftProductType, blank=True, null=True)
    name = models.CharField(max_length=128)
    unique_item = models.BooleanField(default=0)
    comment = models.CharField(max_length=2048, blank=True, null=True)
    deleted = models.BooleanField(default=0)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)

    @property
    def get_type_name(self):
        return "Item"


# Shield
class WikiCraftProduct(models.Model):
    id_wikiCraftProduct = models.AutoField(primary_key=True)
    id_wikiItem = models.ManyToManyField(WikiItem)
    id_wikiCraftProductType = models.ForeignKey(WikiCraftProductType, blank=True, null=True)
    name = models.CharField(max_length=128)
    comment = models.CharField(max_length=2048)
    count = models.IntegerField(default=1)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    deleted = models.BooleanField(default=0)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)
    x_user = models.ForeignKey(settings.AUTH_USER_MODEL)

    @property
    def get_type_name(self):
        return WikiCraftProductType.objects.filter(id_wikiCraftProductType=self.id_wikiCraftProductType)
