# -*- coding: utf-8 -*-
from django.conf.urls import url
from questions import views

urlpatterns = [
    url('', views.index),
]