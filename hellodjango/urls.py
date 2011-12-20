from django.conf.urls.defaults import patterns, include, url
from django.contrib.admindocs import urls
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from impowered.views import home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
     url(r'^impowered/', include('hellodjango.impowered.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^$', home),
     
)
