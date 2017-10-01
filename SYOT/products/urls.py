from django.conf.urls import url
from products import views

urlpatterns = [
    url(r'^$',views.product, name='product'),  #ไว้เรียกหน้า product
]
