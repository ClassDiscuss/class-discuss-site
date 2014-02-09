from django.conf.urls import patterns, url

from class_discuss_site import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login')
)