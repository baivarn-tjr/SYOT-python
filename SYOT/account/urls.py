from django.conf.urls import url
from account import views

app_name = 'acc'

urlpatterns = [
    url(r'^$',views.logout, name = 'logout'),
    url(r'^login/$',views.login, name = 'login'),
    url(r'^signUp/$',views.signup, name = 'signup'),
    url(r'^editProfile/$',views.edit, name = 'edit'),
    url(r'^forgotPass/$',views.forgot, name = 'forgot'),
    url(r'^profile/$',views.profile, name = 'profile'),
    url(r'^login_check/$',views.loginCheck, name = 'logincheck'),
    url(r'^forgot_check/$',views.forgotCheck, name = 'forgotcheck'),
    url(r'^reset_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.reset_password, name='reset_password'),
    url(r'^activated_acc/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activated_acc, name='activated_acc'),
]
