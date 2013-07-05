from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
	url(r'^(?P<news_id>\d+)/$', views.news_page, name='newspage'),
	#url(r'^add_news/$', views.add_news, name='addnews')
	)