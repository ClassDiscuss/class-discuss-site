from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'ClassDiscuss.views.home', name='home'),
    url(r'^discussions/', include('class_discuss_site.discussion_urls')),
    url(r'^users/', include('class_discuss_site.user_urls')),
    url(r'^courses/', include('class_discuss_site.course_urls')),
    url(r'^login/', include('class_discuss_site.login_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('class_discuss_site.index_url')),
)
