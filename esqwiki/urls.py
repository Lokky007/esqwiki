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

    url(r'^$', include("main.urls"), ),
    url(r'^main/', include("main.urls"), name='main'),
    url(r'^board/', include("board.urls"), name='board'),
    url(r'^wiki/', include("wiki.urls"), name='wiki'),
    url(r'^auction/', include("auction.urls"), name='auction'),
    url(r'^trade/', include("trade.urls"), name='trade'),
    url(r'^forum/', include("forum.urls"), name='forum'),
    url(r'^map/', include("worldmap.urls"), name='worldmap'),
    url(r'^detail/', include('userGuildDetail.urls', namespace="userGuildDetail")),
    url(r'^questions/', include('questions.urls', namespace="questions")),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
