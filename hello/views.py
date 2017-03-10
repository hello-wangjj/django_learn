from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from hello.models import *
from hello.form import PublisherForm
import datetime
# Create your views here.


def hello_table(request):
    user_list = User.objects.all()
    time = datetime.datetime.now()
    url_baidu = "<a href='http://www.baidu.com'>百度</a>"
    user_info = {
        'user_list': user_list,
        'if_test': 1,
        'time': time,
        'url_baidu': url_baidu
    }
    # print(user_info)
    return render(request, 'table.html', user_info)


def add_publisher(request):
    # pass
    if request.method == 'POST':
        # 如果为post提交，去接收用户提交的信息
        # print(request.POST)
        # 不使用form的情况
        # name = request.POST.get('name')
        # address = request.POST.get('address')
        # city = request.POST.get('city')
        # state_province = request.POST.get('state_province')
        # country = request.POST.get('country')
        # website = request.POST.get('website')
        # Publisher.objects.create(
        #     name=name,
        #     address=address,
        #     city=city,
        #     state_province=state_province,
        #     country=country,
        #     website=website
        # )
        # return HttpResponse('添加成功')
        # 使用django from的情况
        # publisher_form = PublisherFrom(request.POST)
        # if publisher_form.is_valid():
        #     Publisher.objects.create(
        #         name=publisher_form.cleaned_data['name'],
        #         address=publisher_form.cleaned_data['address'],
        #         city=publisher_form.cleaned_data['city'],
        #         state_province=publisher_form.cleaned_data['state_province'],
        #         country=publisher_form.cleaned_data['country'],
        #         website=publisher_form.cleaned_data['website']
        #     )
        #     return HttpResponse('添加成功')
        # 使用django ModelFrom的情况
        publisher_form = PublisherForm(request.POST)
        if publisher_form.is_valid():
            publisher_form.save()
            return HttpResponse('添加成功')
    else:
        publisher_form = PublisherForm()
        # publisher_form.fields['name'].label = '名称'
        # publisher_form.fields['address'].label = '地址'
        # publisher_form.fields['city'].label = '城市'
        # publisher_form.fields['state_province'].label = '省份'
        # publisher_form.fields['country'].label = '国家'
        # publisher_form.fields['website'].label = '网址'

    return render(request, 'add_publisher.html', locals())
