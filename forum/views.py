# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from forum.models import CategoryBlock, Category, Topic, Answer


# Create your views here.
def index(request):
    category_array = []
    category_block_data = CategoryBlock.objects.filter(show=1)

    for category_block in category_block_data:
        answer_array = []
        subcategory_data = Category.objects.filter(show=1, id_category_block=category_block.id_category_block)
        for answer in subcategory_data:
            answer_array.append(answer)

        category_array.append([category_block, answer_array])
    return render(request, 'forum_base.html', {'category_data': category_array})


def topic_overview(request, id_category):
    topic_data = Topic.objects.filter(category=id_category, deleted=0)
    return render(request, 'forum_topic_overview.html', {'topic_data': topic_data})


def topic(request,id_category, id_topic):
    topic_data = Topic.objects.filter(id_topic=id_topic, deleted=0)
    answer_data = Answer.objects.filter(topic=id_topic, deleted=0)
    return render(request, 'forum_topic.html',
                  {'answer_data': answer_data,
                   'topic_data': topic_data
                   })
