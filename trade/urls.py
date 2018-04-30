# -*- coding: utf-8 -*-
from django.conf.urls import url
from trade import views

urlpatterns = [
    url('', views.index),
]