from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.loot, name='loot'),
    url(r'^(?P<profile_id>[0-9A-Za-z_\-]+)/$', views.detail, name='detail'),

]
