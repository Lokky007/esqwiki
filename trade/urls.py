# -*- coding: utf-8 -*-
from django.conf.urls import url
from trade import views
from forms import TradeNewSell

urlpatterns = [
    url('', views.index),
]