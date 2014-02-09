from django.conf.urls import patterns, url

from class_discuss_site import views

urlpatterns = patterns('',
    url(r'^$', views.courses, name='courses'),
    url(r'^create$', views.course_create_page, name='course_create_page'),
    url(r'^insert$', views.course_insert, name='course_insert'),
    url(r'^(?P<course_id>\d+)/$', views.course_detail, name='course_detail')
)