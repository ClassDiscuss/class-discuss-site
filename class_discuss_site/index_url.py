from django.conf.urls import patterns, url
from class_discuss_site import views

urlpatterns = patterns('',
    # show the index page
    url(r'^$', views.index_view, name='index')
)