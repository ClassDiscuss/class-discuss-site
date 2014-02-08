from django.conf.urls import patterns, url

from class_discuss_site import views

urlpatterns = patterns('',
    url(r'^$', views.groups, name='groups'),
    # ex: /groups/5/
    url(r'^(?P<group_id>\d+)/$', views.group_detail, name='group_detail')
)