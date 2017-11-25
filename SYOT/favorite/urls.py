from django.conf.urls import url

from . import views

# app_name = 'carts'
urlpatterns = [
    # ex: /polls/
    url(r'^(?P<user_id>[0-9]+)/$', views.favorite, name='favorite'),
    url(r'^delete/$', views.deletefav, name='deletefav'),
    # url(r'^delete/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.deletefav, name='deletefav'),
]
