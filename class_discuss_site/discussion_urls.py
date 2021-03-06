from django.conf.urls import patterns, url

from class_discuss_site import views

urlpatterns = patterns('',
    # show all discussions for the current user
    url(r'^$', views.user_discussions, name='dicussions'),

    # bow out of the discussion
    url(r'^(?P<discussion_id>\d+)/logout/$', views.discussion_detail_logout, name='discussion_detail_logout'),

    # show a specific discussion
    url(r'^(?P<discussion_id>\d+)/$', views.discussion_detail, name='discussion_detail'),

    # show page to start a new discussion
    url(r'^create$', views.discussion_create, name='discussions_create')
)