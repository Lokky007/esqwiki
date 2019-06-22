# -*- coding: utf-8 -*-
from django.conf.urls import url
from forum import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'(?P<id_category>\d+)/$', views.topic_overview, name='topic'),
    url(r'(?P<id_category>\d+)/(?P<id_topic>\d+)$', views.topic, name='topic'),
]