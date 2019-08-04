from django.shortcuts import render
from wiki.models import WikiItem, WikiCraftProduct, WikiCraftProductType
import wiki.classes.globalWikiFunction as wiki_function
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.


def index(request):
    records = WikiCraftProductType.objects.filter().order_by('name')
    return render(request, 'index_page_wiki.html', {
        'wiki_menu': True,
        'crafts_list': records,
    })


def items(request, id_craft):
    if id_craft == 0:
        records = WikiItem.objects.filter(deleted=0).order_by('name')
    else:
        records = WikiCraftProduct.objects.filter(id_wikiCraftProductType=id_craft).order_by('name')

    return render(request, 'index_page_wiki.html', {
        'wiki_content': records,
        'wiki_content_type': id_craft
    })

def items_preview(request):
    return content_for_dynamic_preview(request)


@csrf_exempt
def content_for_dynamic_preview(request):
    response_data = {}
    data = wiki_function.prepare_data_detail_view(request)
    response_data['message'] = wiki_function.prepare_html_detail_view(data).content

    return HttpResponse(json.dumps(response_data), content_type="application/json")
