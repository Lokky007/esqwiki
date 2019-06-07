from django.shortcuts import render
from wiki.models import WikiItem, WikiCraftProduct
import wiki.classes.globalWikiFunction as wiki_function
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.


def index(request):
    return render(request, 'index_page_wiki.html')


def items(request):
    records = WikiItem.objects.filter(deleted=0).order_by('name')
    return render(request, 'index_page_wiki.html', {'wiki_content': records})


def items_preview(request):
    return content_for_dynamic_preview(request)


def blacksmithy(request):
    records = WikiCraftProduct.objects.filter(id_wikiCraftProductType=1).order_by('name')
    return render(request, 'index_page_wiki.html', {'wiki_content': records})


def alchemy(request):
    records = WikiCraftProduct.objects.filter(id_wikiCraftProductType=2).order_by('name')
    return render(request, 'index_page_wiki.html', {'wiki_content': records})


def tailoring(request):
    records = WikiCraftProduct.objects.filter(id_wikiCraftProductType=3).order_by('name')
    return render(request, 'index_page_wiki.html', {'wiki_content': records})


def engeneering(request):
    records = WikiCraftProduct.objects.filter(id_wikiCraftProductType=4).order_by('name')
    return render(request, 'index_page_wiki.html', {'wiki_content': records})

@csrf_exempt
def content_for_dynamic_preview(request):
    response_data = {}
    data = wiki_function.prepare_data_detail_view(request)
    response_data['message'] = wiki_function.prepare_html_detail_view(data).content

    return HttpResponse(json.dumps(response_data), content_type="application/json")
