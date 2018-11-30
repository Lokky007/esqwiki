from django.shortcuts import render
from django.http import HttpResponse
from wiki.models import WikiCraftProduct,WikiItem


# Create your views here.
def index(request):
    records_items = WikiItem.objects.filter().order_by('-x_created')
    records_products = WikiCraftProduct.objects.filter().order_by('-x_created')

    list_news = []
    for row in records_items:
        list_news.append(row)

    for row in records_products:
        list_news.append(row)

    return render(request, 'main_base.html', {'newest_records': list_news})
