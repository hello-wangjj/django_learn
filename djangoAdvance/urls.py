#!python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from djangoAdvance import views
__author__ = 'wangjj'
__mtime__ = '2017031413:34'
urlpatterns = [
    url(r'^advance1/$', views.advance1, name='advance1')
]
