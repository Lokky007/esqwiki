from django.shortcuts import render
from django.http import HttpResponse
from wiki.models import WikiCraftProduct, WikiItem
from board.models import posts
from main.models import ProjectTasks


# Create your views here.
def index(request):
    news = get_news()
    tasks = get_tasks()
    return render(request, 'main_base.html', {'newest_records': news,
                                              'user':  request.user,
                                              'actual_tasks': tasks})


def get_news():
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

    return list_news


def get_tasks():
    return ProjectTasks.objects.filter().order_by('-x_created')[:10]


def getKey(item):
    return item[2]