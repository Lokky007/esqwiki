from django.shortcuts import render
from django.http import HttpResponse
from wiki.models import WikiCraftProduct, WikiItem
from board.models import posts


# Create your views here.
def index(request):
    records_items = WikiItem.objects.filter().order_by('-x_created')[:5]
    records_products = WikiCraftProduct.objects.filter().order_by('-x_created')[:5]
    records_questions = posts.objects.filter().order_by('-x_created')[:5]

    list_news = []
    for row in records_items:
        list_news.append([row.name, row.x_user.username, row.x_created, 'Item'])

    for row in records_products:
        list_news.append([row.name, row.x_user.username, row.x_created, 'Product'])

    for row in records_questions:
        list_news.append([row.text, row.x_user.username, row.x_created, 'Questionatire'])

    sorted(list_news, key=getKey, reverse=True)

    return render(request, 'main_base.html', {'newest_records': list_news})


def getKey(item):
    return item[2]