from django.conf.urls import url
from django.contrib import admin

from webSite.views import *

urlpatterns = [
    url(r'post_index/$', post_index, name='post_index'),
    url(r'$', index, name='index')
]
