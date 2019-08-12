from django.conf.urls import url, include
from django.contrib import admin
from loginRegistration import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^login/$', views.Login, name='Login'),
    url(r'^registration/$', views.Register, name='Register'),
    url(r'^logout/$', views.Logout, name='Logout'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    #url('^', include("main.urls"), name='main'),
    url('^main/', include("main.urls"), name='main'),
    url('^board/', include("board.urls"), name='board'),
    url('^wiki/', include("wiki.urls"), name='wiki'),
    url('^auction/', include("auction.urls"), name='auction'),
    url('^trade/', include("trade.urls"), name='trade'),
    url('^forum/', include("forum.urls"), name='forum'),
    url('^map/', include("worldmap.urls"), name='worldmap'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
