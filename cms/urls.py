from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pendingArticles, name='cmsHome'),
    url(r'^(?P<a_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<a_id>[0-9]+)/approve$', views.approve, name='approve'),
    url(r'^(?P<a_id>[0-9]+)/reject$', views.reject, name='reject'),
]