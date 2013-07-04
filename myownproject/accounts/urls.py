from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
	url(r'^registration$', views.registration, name='registration'),
	#url(r'^login$', views.login, name='login'),
	#url(r'^logout$', views.logout, name='logout'),
)