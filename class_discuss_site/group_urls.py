from django.conf.urls import patterns, url

from class_discuss_site import views

urlpatterns = patterns('',
    url(r'^$', views.groups_view, name='groups'),
    url(r'^(?P<group_id>\d+)/$', views.group_detail, name='group_detail'),
    url(r'^(?P<group_id>\d+)/insert$', views.group_post_message, name='group_post_message')
)