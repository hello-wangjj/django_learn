"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ganji.views import index
from pure.views import pure, pure_statistics
from semantic_ui.views import semantic, new_data, new_chart
from learn import views as learn_views
from hello import views as hello_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^pure/', pure),
    url(r'^pure_statistics/', pure_statistics),
    url(r'^semantic_ui/', semantic),
    url(r'^new_data/', new_data),
    url(r'^new_chart/', new_chart),
    url(r'^learn_add/$', learn_views.add, name='add'),
    url(r'^learn_add/(\d+)/(\d+)/$', learn_views.old_add2_redirect),
    url(r'^learn_home/$', learn_views.home, name='home'),
    url(r'^learn_new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    url(r'^hello_table/$', hello_views.hello_table, name='hello_table'),
    url(r'^hello/', include('hello.urls'))

]
