from django.shortcuts import render
from ganji.models import ArticleInfo
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    limit = 4
    article_info = ArticleInfo.objects
    print(article_info[0].title, len(article_info))
    paginator = Paginator(article_info, limit)
    page = request.GET.get('page', 1)
    print(request)
    print(request.GET, page)
    loaded = paginator.page(page)
    context = {
        'article_info': loaded
    }
    return render(request, 'index.html', context)
