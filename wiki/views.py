from django.shortcuts import render
from wiki.models import WikiItem

# Create your views here.


def index(request):
    return render(request, 'index_page_wiki.html')


def items(request):
    records = WikiItem.objects.filter(deleted=0).order_by('name')

    return render(request, 'index_page_wiki.html', {'wiki_content': records})


def blacksmithy(request):
    return render(request, 'index_page_wiki.html', {'wiki_content': 'blacksmithy'})


def alchemy(request):
    return render(request, 'index_page_wiki.html', {'wiki_content': 'alchemy'})


def tailoring(request):
    return render(request, 'index_page_wiki.html', {'wiki_content': 'tailoring'})


def engeneering(request):
    return render(request, 'index_page_wiki.html', {'wiki_content': 'engeneering'})