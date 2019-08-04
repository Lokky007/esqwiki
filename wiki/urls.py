# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from wiki import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'items/(?P<id_craft>\d+)/$', views.items, name='wiki'),
    url(r'items_preview/$', views.items_preview, name='wiki_item_preview'),

]