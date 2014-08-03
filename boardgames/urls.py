from django.conf.urls import patterns, include, url

from .views import HelloWorldView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', HelloWorldView.as_view(), name='boardgames_home'),
	#url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
	#this is like an inline import
	'django.contrib.auth.views',
	url(r'^login/$', 'login', #this is the view
	    {'template_name': 'login.html'}, #template to link to
	    name='boardgames_login'), # name of url mapping
	url(r'^logout/$', 'logout',
	    {'next_page': 'boardgames_home'},
	    name='boardgames_logout'),
)
