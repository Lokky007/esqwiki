# -*- coding: utf-8 -*-
from django.conf.urls import url
from board import views

urlpatterns = [
    url('', views.index),
    url('delete', views.index),
]