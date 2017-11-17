from django.conf.urls import url
from testuser import views

app_name = 'test'

urlpatterns = [
    # url(r'^$',views.logout, name = 'logout'),
    url(r'^$',views.loginIndex, name = 'loginIndex'),
    url(r'^login/$',views.login, name = 'login'),
    # url(r'^signUp/$',views.signup, name = 'signup'),
    # url(r'^forgotPass/$',views.forgot, name = 'forgot'),
    # url(r'^login/check/$',views.loginCheck, name = 'logincheck'),
    # url(r'^signUp/check/$',views.signupCheck, name = 'signupcheck'),
]
