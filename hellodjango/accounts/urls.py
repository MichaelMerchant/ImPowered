from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
#from map_volunteering.models import Profile
from accounts.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('accounts.views',

     url(r'^login/$', myLogin, name='login'),
     url(r'^logout/$', myLogout, name='logout'),
     

)
