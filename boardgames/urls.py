from django.conf.urls import patterns, include, url

#from .views import HelloWorldView
from .views import HomePageView
from .views import LoggedOutView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', HomePageView.as_view(), name='boardgames_home'),
    #url(r'^logout/', LoggedOutView.as_view(), name='boardgames_logged_out'), this doesn't work for some reason
	#url(r'^blog/', include('blog.urls')),
    url(r'^my_user/', include('my_user.urls')),
	url(r'^admin/', include(admin.site.urls)),
)

# can add patterns with +=
# patterns function has a prefix string as a first argument
# views can receive keyword arguments
# urls can be named

urlpatterns += patterns(
	#this is like an inline import
	'django.contrib.auth.views', 
    #longform for this is not "login" but "django.contrib.auth.views.login"
	url(r'^login/$', 'login', #this is the view
	    {'template_name': 'login.html'}, #template to link to
	    name='boardgames_login'), # name of url mapping
	url(r'^logout/$', 'logout',
	    {'next_page': 'boardgames_home'},
	    name='boardgames_logout'),
)
