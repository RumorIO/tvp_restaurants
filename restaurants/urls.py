from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

urlpatterns = patterns('',
   (r'^$', 'view'),
)