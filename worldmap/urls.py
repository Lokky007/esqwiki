# -*- coding: utf-8 -*-
from django.conf.urls import url
from worldmap import views

urlpatterns = [
    url('', views.index),
]