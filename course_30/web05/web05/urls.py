from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web05.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^disp/$', 'blog.views.disp', {'id': '1234', 'name': 'nobody'}),
    url(r'^disp/(?P<id>\d+)/(?P<name>\w+)/$', 'blog.views.disp'),
    url(r'^regist/$', 'blog.views.regist'),
)
