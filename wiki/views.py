from django.shortcuts import render
from wiki.models import WikiItem, WikiCraftProduct, WikiCraftProductType
import wiki.classes.globalWikiFunction as wiki_function
from django.views.decorators.csrf import csrf_exempt
from wiki.forms import WikiNewRecord
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
    id_craft= int(id_craft)
    if id_craft == 1:
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


def items_new_record(request, id_type):
    id_type = int(id_type)

    if request.method == 'POST':
        wiki_new_record = WikiNewRecord(request.POST)
        if id_type == 1:
            add_item(request, wiki_new_record, id_type)

    wiki_new_record = WikiNewRecord()
    return render(request, 'new_record.html', {
        'new_record': wiki_new_record
    })


def add_item(request, wiki_new_record, id_type):
    if wiki_new_record.is_valid():
        name = wiki_new_record.cleaned_data.get("name")
        unique_item = wiki_new_record.cleaned_data.get("unique_item")
        comment = wiki_new_record.cleaned_data.get("comment")
        image = wiki_new_record.cleaned_data.get("image")

        wiki_type = WikiCraftProductType.objects.get(id_wikiCraftProductType=id_type)

        new_wiki_item = WikiItem(name=name, id_wikiCraftProductType=wiki_type,
                                 unique_item=unique_item, comment=comment, image=image,
                                 deleted=0, x_user=request.user)
        new_wiki_item.save()
