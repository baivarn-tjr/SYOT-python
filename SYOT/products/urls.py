from django.conf.urls import url , include
from products import views
from SYOT import views as syot_views

# app_name = 'Product'

urlpatterns = [
    # url(r'^index/$',views.index, name='index'),
    # url(r'^$',syot_views.index, name='index'),
    url(r'^products/$',views.catalog, name='product'),  #ไว้เรียกหน้า product
    url(r'^detail/(?P<product_id>[0-9]+)/$', views.detail , name = 'detail'),
    url(r'^products/search/',views.search, name='search'),
    url(r'^addtocart/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.addtocart, name='addtocart'),
    url(r'^addtofav/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.addtofav, name='addtofav'),

]
