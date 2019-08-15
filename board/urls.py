# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from board import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^delete/(?P<id_post>\d+)/$', views.delete_post, name='Delete file'),
    url(r'^writeAnswer/(?P<id_post>\d+)/$', views.answer, name='Answer'),
    url(r'^writeComment/(?P<id_post>\d+)/$', views.comment, name='Comment'),
]
