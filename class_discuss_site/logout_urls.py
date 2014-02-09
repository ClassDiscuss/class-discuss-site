from django.conf.urls import patterns, url

from class_discuss_site import views

urlpatterns = patterns('',
    # display the login page
    url(r'^$', views.logout_view, name='logout_view')
)