#!python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from hello import views
__author__ = 'wangjj'
__mtime__ = '2017022820:17'
urlpatterns = [
    url(r'^hello_table2/$', views.hello_table, name='hello_table_2'),
    url(r'^add_publisher/$', views.add_publisher, name='add_publisher')
]
