from django.conf.urls import patterns, include, url

urlpatterns = patterns('my_user.views',
    url(r'^home$', 'home', name='my_user_home')
)
