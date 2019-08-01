# -*- coding: utf-8 -*-
from django.conf.urls import url
from forum import views

urlpatterns = [
    url(r'^$', views.index, name='main_forum'),
    url(r'(?P<id_category>\d+)/$', views.topic_overview, name='topic_overview'),
    url(r'(?P<id_category>\d+)/(?P<id_topic>\d+)$', views.topic, name='topic'),


    url(r'topic/new/(?P<id_category>\d+)$', views.new_topic, name='new_topic'),
    url(r'topic/answer/(?P<id_category>\d+)/(?P<id_topic>\d+)$', views.new_answer, name='new_answer'),
    url(r'topic/answer/delete/(?P<id_answer>\d+)$', views.delete_answer,
        name='delete_answer'),
]
