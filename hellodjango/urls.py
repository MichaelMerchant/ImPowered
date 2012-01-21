from django.conf.urls.defaults import patterns, include, url
from django.contrib.admindocs import urls
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()

def home(request):
    return render(request, "index.html")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
     url(r'^impowered/', include('hellodjango.impowered.urls')),
     url(r'^pairing/', include('hellodjango.pairing.urls')),
     url(r'^eweekmap/', include('map_volunteering.urls')),
     url(r'^accounts/', include('accounts.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     

     url(r'^$', home, name='home'),
     
)

