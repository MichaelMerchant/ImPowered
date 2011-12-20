from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from impowered.models import Profile
from impowered.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('impowered.views',

     url(r'^$', 'home', name='home'),
     url(r'^skill_tree$', 'skill_tree', name='skill_tree'),
     url(r'^skill_tree/(?P<userid>\d+)/(?P<rootid>\d+)/$', 'skill_tree_user', name='skill_tree_user'),
     url(r'^skill_tree2$', 'skill_tree2', name='skill_tree2'),

)
