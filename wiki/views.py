from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.


def index(request):
    return render(request, 'index_page_wiki.html')


def blacksmithy(request):
    return render(request, 'index_page_wiki.html', {'wiki_content': 'blacksmithy'})


def alchemy(request):
    return render(request, 'index_page_wiki.html', {'wiki_content': 'alchemy'})


def tailoring(request):
    return render(request, 'index_page_wiki.html', {'wiki_content': 'tailoring'})


def engeneering(request):
    return render(request, 'index_page_wiki.html', {'wiki_content': 'engeneering'})