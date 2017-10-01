from django.conf.urls import url
from products import views

# app_name = 'Product'

urlpatterns = [
    url(r'^index/$',views.index, name='index'),
    url(r'^products/$',views.catalog, name='product'),  #ไว้เรียกหน้า product
    url(r'^detail/(?P<product_id>[0-9]+)/$', views.detail , name = 'detail'),
<<<<<<< HEAD
    url(r'^products/search/',views.search, name='search'),
=======
    url(r'^addtocart/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.addtocart, name='addtocart'),

>>>>>>> ee816fd3a727dacd3f51cbebdea82a6a5ba2407b
]
