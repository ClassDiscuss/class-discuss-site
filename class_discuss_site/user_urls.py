from django.conf.urls import patterns, url
from class_discuss_site import views

urlpatterns = patterns('',
    url(r'^$', views.users, name='users'),
    url(r'^(?P<username>\w+)/$', views.user_detail, name='username')
)