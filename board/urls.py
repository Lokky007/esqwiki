# -*- coding: utf-8 -*-
from django.conf.urls import url
from board import views

urlpatterns = [
    url(r'^delete/(?P<id_post>\d+)/$', views.delete_post, name='Delete file'),
    url(r'^$', views.index),
]