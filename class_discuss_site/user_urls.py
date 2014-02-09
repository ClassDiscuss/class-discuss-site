from django.conf.urls import patterns, url
from class_discuss_site import views

urlpatterns = patterns('',
    # show a profile for the user
    url(r'^(?P<username>\w+)/$', views.user_detail, name='username')
)