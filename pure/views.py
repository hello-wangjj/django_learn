from django.shortcuts import render

# Create your views here.


def pure(request):
    return render(request, 'pure.html')
