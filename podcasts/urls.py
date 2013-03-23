from django.conf.urls import patterns, include, url

from podcasts import views

urlpatterns = patterns('',
 		#home page
 		# url(r'^$', views.index, name='index'),
 		#podcast channel page 
 		# url(r'^?P<channel>\d+)/$', views.channel, name='channel'),
 		#podcast rss feed
 		url(r'^(?P<channel_id>\d+)/rss',views.rss, name="rss"),

 	)