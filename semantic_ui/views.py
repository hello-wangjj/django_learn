from django.shortcuts import render
from semantic_ui.models import ItemInfo, last_pub_date
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


def new_data(request):
    limit = 10
    item_info = ItemInfo.objects
    paginator = Paginator(item_info, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    item_info = {
        'item_info': loaded,
        'counts': item_info.count(),
        'last_date': last_pub_date[0]

    }
    print(item_info)
    return render(request, 'new_data.html', item_info)

# 获取不同地区的发帖量前三名


def top_x(date1, date2, area, limit):
    pipeline = [
        {'$match': {'$and': [{'pub_date': {'$gt': date1, '$lt': date2}}, {'area': {'$all': area}}]}},
        {'$group': {'_id': {'$slice': ['$cates', 2, 1]}, 'counts': {'$sum': 1}}},
        {'$sort': {'counts': -1}},
        {'$limit': limit}
    ]
    for i in ItemInfo._get_collection().aggregate(pipeline):
        data = {
            'name': i['_id'][0],
            'data': [i['counts']],
            # 'type': 'column'
        }
        yield data
series_CY = [i for i in top_x('2015.12.25', '2016.01.10', ['朝阳'], 3)]
series_TZ = [i for i in top_x('2015.12.25', '2016.01.10', ['通州'], 3)]
series_HD = [i for i in  top_x('2015.12.25', '2016.01.10', ['海淀'], 3)]


def new_chart(request):
    context = {
        'chart_CY': series_CY,
        'chart_TZ': series_TZ,
        'chart_HD': series_HD
    }

    return render(request, 'new_chart.html',context)
