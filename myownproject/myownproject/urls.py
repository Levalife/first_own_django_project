from django.conf.urls import patterns, include, url
from accounts.views import logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myownproject.views.home', name='home'),
    # url(r'^myownproject/', include('myownproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^news/', include('news.urls', namespace='news')),
)
