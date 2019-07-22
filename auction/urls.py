# -*- coding: utf-8 -*-
from django.conf.urls import url
from auction import views

urlpatterns = [
    url('', views.index),
]