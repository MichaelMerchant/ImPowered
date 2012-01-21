from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from pairing.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('pairing.views',

     url(r'^$', 'home', name='pairing_home'),
     url(r'^project/(?P<project_id>\d+)/$', 'student_listing', name='student_listing'),
     url(r'^row/(?P<other_sid>\d+)/(?P<pid>\d+)/$', 'student_row', name='row'),
     url(r'^invite/(?P<sid>\d+)/(?P<pid>\d+)/$', 'invite', name='invite'),
     url(r'^accept/(?P<sid>\d+)/(?P<pid>\d+)/$', 'accept', name='accept'),
     url(r'^cancel/(?P<sid>\d+)/(?P<pid>\d+)/$', 'cancel', name='cancel'),

)