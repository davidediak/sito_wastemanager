from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'signup/', views.SignUp.as_view(), name='signup'),
    url(r'^(?P<u_id>[0-9]+)/$', views.profile, name='profile'),
]