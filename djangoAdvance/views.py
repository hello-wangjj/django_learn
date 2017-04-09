from django.shortcuts import render

# Create your views here.
def advance1(request):

    return render(request,'advance1.html',locals())