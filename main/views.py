from django.shortcuts import render
from django.http import HttpResponse
from wiki.models import WikiCraftProduct, WikiItem
from forum.models import Topic
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
    records_topic = Topic.objects.filter().order_by('-x_created')[:5]

    return {"items": records_items,
            "products": records_products,
            "topic": records_topic
    }


def get_tasks():
    return ProjectTasks.objects.filter().order_by('-x_created')[:10]


def getKey(item):
    return item[2]
