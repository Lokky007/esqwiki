# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from userGuildDetail import views

urlpatterns = [
    url(r'^user/(?P<id_user>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^guild/(?P<id_guild>\d+)/$', views.guild_detail, name='guild_detail'),

]