from django.conf.urls import url
from account import views

app_name = 'acc'

urlpatterns = [
    url(r'^login/$',views.login, name = 'login'),
    url(r'^login/check/$',views.loginCheck, name = 'logincheck'),
    url(r'^login/test/$',views.test, name = 'test'),
]
