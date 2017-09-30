from django.conf.urls import url
from products import views

# app_name = 'Product'

urlpatterns = [
    url(r'^$',views.index, name='product'),  #ไว้เรียกหน้า product
    url(r'^detail/(?P<product_id>[0-9]+)/$', views.detail , name = 'detail'),
]
