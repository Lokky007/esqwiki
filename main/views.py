from django.shortcuts import render
from django.http import HttpResponse
from wiki.models import WikiCraftProductType

# Create your views here.
def index(request):
    records = WikiCraftProductType.objects.filter().order_by('-x_created')

    list_news = []
    for row in records:
        list_news.append(row)

    return render(request, 'main_base.html', {'newest_records': list_news})
