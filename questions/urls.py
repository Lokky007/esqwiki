# -*- coding: utf-8 -*-
from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'rightAnswer/$', views.right_answer, name="right_answer"),
]