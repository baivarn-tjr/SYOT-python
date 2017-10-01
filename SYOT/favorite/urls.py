from django.conf.urls import url

from . import views

# app_name = 'carts'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.favorite, name='favorite'),
    url(r'^delete/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.deletefav, name='deletefav'),
]
