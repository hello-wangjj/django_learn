from django.shortcuts import render
from semantic_ui.models import ItemInfo
from django.core.paginator import Paginator
# Create your views here.


def semantic(request):
    limit = 10
    item_info = ItemInfo.objects
    paginator = Paginator(item_info, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    item_info = {
        'item_info': loaded
    }

    return render(request, 'semantic_web.html', item_info)
