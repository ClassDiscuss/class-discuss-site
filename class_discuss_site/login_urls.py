from django.conf.urls import patterns, url

from class_discuss_site import views

urlpatterns = patterns('',
    url(r'^$', views.login_request, name='login_request'),
    url(r'^authenticate/', views.authenticate_request, name='authenticate_request')
)