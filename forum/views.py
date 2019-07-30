# -*- coding: utf-8 -*-

from django.shortcuts import render
from forum.models import CategoryBlock, Category, Topic, Answer
from extension.popup.popup_window import popup
from forms import NewPost
from django.http import HttpResponse, JsonResponse

# Categorie a kategory block
def index(request):
    category_array = []
    category_block_data = CategoryBlock.objects.filter(show=1)

    for category_block in category_block_data:
        answer_array = []
        subcategory_data = Category.objects.filter(show=1, id_category_block=category_block.id_category_block)
        for answer in subcategory_data:
            answer_array.append(answer)

        category_array.append([category_block, answer_array])
    return render(request, 'forum_base.html', {
        'category_data': category_array,
    })


def topic_overview(request, id_category):
    new_post_form = NewPost()

    window = popup(request)
    window.set_form(new_post_form, 'Nový příspěvek', 'new_topic')
    window.set_url_params({'id_category': 1})
    window_html = window.create()

    topic_data = Topic.objects.filter(category=id_category, deleted=0)
    return render(request, 'forum_topic_overview.html', {
        'topic_data': topic_data,
        'popup_window': window_html
    })


def topic(request,id_category, id_topic):
    topic_data = Topic.objects.filter(id_topic=id_topic, deleted=0)
    answer_data = Answer.objects.filter(topic=id_topic, deleted=0)

    return render(request, 'forum_topic.html',{
        'answer_data': answer_data,
        'topic_data': topic_data,
    })


def new_topic(request, id_category):
    if request.method == 'POST':
        new_post = NewPost(request.POST)
        if new_post.is_valid():
            name = new_post.cleaned_data.get("name")
            text = new_post.cleaned_data.get("text")
            record = Topic(name=name, text=text, category_id=id_category, x_user_id=request.user.id)
            record.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': True})
