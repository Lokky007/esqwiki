from django.conf.urls import url, include
from django.contrib import admin
from loginRegistration import views

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^login/$', views.Login, name='Login'),
    url(r'^registration/$', views.Register, name='Register'),
    url(r'^logout/$', views.Logout, name='Logout'),

    url('main/', include("main.urls"), name='main'),
    url('board/', include("board.urls"), name='board'),
]