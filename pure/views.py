from django.shortcuts import render
from django.core.paginator import Paginator
from pure.models import ItemInfo

# Create your views here.


def pure(request):
    return render(request, 'pure.html')


def pure_statistics(request):
    limit = 10
    item_info = ItemInfo.objects
    paginator = Paginator(item_info, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    context = {
        'item_info': loaded
    }

    return render(request, 'pure_statistics.html', context)
