from django.conf.urls import patterns, url
from news import views
#from comments.views import add_comment


urlpatterns = patterns('',
	url(r'^(?P<news_id>\d+)/$', views.news_page, name='newspage'),
	url(r'^add_news/$', views.add_news, name='addnews'),
	url(r'^edit_news/(?P<news_id>\d+)/$', views.edit_news, name='editnews'),
	url(r'^tag/(?P<tag_id>\d+)/$', views.news_by_tag, name='tag'),
	url(r'^category/(?P<category_id>\d+)/$', views.news_by_cat, name='category'),
	#url(r'^(?P<news_id>\d+)/comment/$' , add_comment, name='addcomment')
	)