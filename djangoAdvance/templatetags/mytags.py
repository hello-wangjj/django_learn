#!python3
# -*- coding: utf-8 -*-
from django import template
from datetime import datetime
__author__ = 'wangjj'
__mtime__ = '2017031413:48'
register=template.Library()
class DateNode(template.Node):
    def __init__(self,format_string):
        self.format_string=format_string

    def render(self, context):
        return datetime.now().strftime(self.format_string)

def dateAdvance(parse,token):
    