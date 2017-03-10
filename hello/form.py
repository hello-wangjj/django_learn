#!python3
# -*- coding: utf-8 -*-
from django import forms
from hello.models import *
from django.core.exceptions import ValidationError
__author__ = 'wangjj'
__mtime__ = '201703100:41'

# 表单字段的验证器


def validate_name(value):
    try:
        Publisher.objects.get(name=value)
        raise ValidationError('%s的信息已存在' % value)
    except Publisher.DoesNotExist:
        pass

# class PublisherForm(forms.Form):
#     name = forms.CharField()
#     address = forms.CharField()
#     city = forms.CharField()
#     state_province = forms.CharField()
#     country = forms.CharField()
#     website = forms.URLField()

# ModelForm


class PublisherForm(forms.ModelForm):
    # 表单字段的验证器
    # name = forms.CharField(label='名称', validators=[validate_name])
    # 二、clean_fieldname,验证字段，针对某个字段验证

    # def clean_name(self):
    #     value = self.cleaned_data['name']
    #     try:
    #         Publisher.objects.get(name=value)
    #         raise ValidationError('已存在出版社:%s' % value)
    #     except Publisher.DoesNotExist:
    #         pass
    #     return value
    # 三、表单clean方法，可针对整个表单进行验证。
    def clean(self):
        cleaned_data = super(PublisherForm, self).clean()
        value = cleaned_data.get('name')
        try:
            Publisher.objects.get(name=value)
            self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
        except Publisher.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = Publisher
        exclude = ('id',)
