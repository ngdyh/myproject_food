"""authot:
   data:
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dishes_search/(?P<id1>\d)(?P<id2>\d)(?P<id3>\d)(?P<id4>\d)/$', views.Dishes_search.as_view(), name='dishes_search'),


]
