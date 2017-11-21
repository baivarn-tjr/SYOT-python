from django.conf.urls import url

from . import views

# app_name = 'carts'
urlpatterns = [
    # ex: /polls/
    url(r'^/(?P<user_id>[0-9]+)/$', views.cart, name='carts'),
    url(r'^addminusQuantity/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.addminusQuantity, name='addminusQuantity'),
    url(r'^delete/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.delete, name='delete'),
]
