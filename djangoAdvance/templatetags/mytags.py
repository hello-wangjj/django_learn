#!python3
# -*- coding: utf-8 -*-
from django import template
from datetime import datetime
__author__ = 'wangjj'
__mtime__ = '2017031413:48'
register = template.Library()


class DateNode(template.Node):

    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        return datetime.now().strftime(self.format_string)


def dateAdvance(parse, token):
    try:
        tag_name, fromat_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('invalid args')
    return DateNode(fromat_string[1:-1])
register.tag(name='myDate', compile_function=dateAdvance)
