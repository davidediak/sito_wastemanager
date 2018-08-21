from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^write/', views.write, name='write'),
    url(r'^(?P<a_id>[0-9]+)/$', views.detail, name='detail'),
   # url(r'^modify/(?P<a_id>[0-9]+)/$', views.modify, name='modify'),
    # url(r'^(?P<a_id>[0-9]+)/approve$', views.approve, name='approve'),
    # url(r'^(?P<a_id>[0-9]+)/reject$', views.reject, name='reject'),
]