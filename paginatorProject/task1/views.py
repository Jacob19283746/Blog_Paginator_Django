from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

def newsedge(request):
    per_page = request.GET.get('per_page', 3)
    per_page = int(per_page)
    news = News.objects.all().order_by('-date_time')
    paginator = Paginator(news, per_page)
    page_number = request.GET.get('page', 1)
    page_object = paginator.get_page(page_number)
    context = {
        'page_object': page_object,
        'per_page': per_page
    }
    return render(request, 'newsedge.html', context)

