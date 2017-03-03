#!python3
# -*- coding: utf-8 -*-
import os
__author__ = 'wangjj'
__mtime__ = '2017030321:07'


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)
