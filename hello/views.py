from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def hello_table(request):
    user_list = User.objects.all()
    user_info = {
        'user_list': user_list
    }
    return render(request, 'table.html', user_info)
