from django.conf.urls import url
from django.contrib import admin

from webSite.views import *

urlpatterns = [
    url(r'$', index, name='index')
]
