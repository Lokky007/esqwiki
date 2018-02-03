# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from wiki import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'items/$', views.items, name='wiki'),
    url(r'items_preview/$', views.items_preview, name='wiki_item_preview'),
    url(r'blacksmithy/$', views.blacksmithy, name='wiki'),
    url(r'alchemy/$', views.alchemy, name='wiki'),
    url(r'tailoring/$', views.tailoring, name='wiki'),
    url(r'engeneering/$', views.engeneering, name='wiki'),
]