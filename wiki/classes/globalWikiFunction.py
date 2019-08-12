# -*- coding: utf-8 -*-
from wiki.models import WikiItem, WikiCraftProduct
from django.shortcuts import render_to_response


def prepare_data_detail_view(request):
    try:
        id = int(request.POST['record_id'])
        type_id = int(request.POST['type_product_id'])

        if type_id == 1:
            records = WikiItem.objects.filter(deleted=0, id_wikiItem=id)
        else:
            records = WikiCraftProduct.objects.filter(deleted=0, id_wikiCraftProduct=id, id_wikiCraftProductType=type_id)
    except:
        records = None

    if not records:
        return
    return records


def prepare_html_detail_view(data):
    return render_to_response('detail_item_wiki.html', {'content': data})
