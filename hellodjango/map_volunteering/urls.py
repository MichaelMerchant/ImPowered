from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
#from map_volunteering.models import Profile
from map_volunteering.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('map_volunteering.views',

     url(r'^$', 'home', name='map_home'),
     url(r'^test$', 'test',name='test'),

)
