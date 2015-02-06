from django.conf.urls import patterns, include, url
from django.contrib import admin

# from blog.views import index

urlpatterns = patterns('',
	#'blog.views'
    # Examples:
    # url(r'^$', 'web04.views.home', name='home'),
	url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/\d{3}/$', 'index'),
    #url(r'^index/$', index)
)

'''
urlpatterns += patterns('', 
	url(r'^index/$', index), 
)
'''