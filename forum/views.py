# -*- coding: utf-8 -*-

from django.shortcuts import render
from forum.models import CategoryBlock, Category, Topic, Answer, Reaction
from extension.popup.popup_window import popup
from forms import NewPost, AnswerOnPost, NewReaction
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect


# Category block
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
    window.set_url_params({'id_category': id_category})
    window_html = window.create()

    topic_data = Topic.objects.filter(category=id_category, deleted=0).order_by('-x_created')
    return render(request, 'forum_topic_overview.html', {
        'topic_data': topic_data,
        'popup_window': window_html
    })


# detail of topic with response threat
def topic(request, id_category, id_topic):
    topic_data = Topic.objects.filter(id_topic=id_topic, deleted=0)
    answer_data = Answer.objects.filter(topic=id_topic, deleted=0)
    reaction_data = Reaction.objects.filter(answer__in=answer_data, deleted=0)
    new_answer_post = new_answer(request, id_category, id_topic)

    new_reaction_form = new_reaction(request)


    return render(request, 'forum_topic.html', {
        'answer_data': answer_data,
        'topic_data': topic_data,
        'reaction_data': reaction_data,
        'id_category': id_category,
        'id_topic': id_topic,
        'new_answer_post': new_answer_post,
        'new_reaction_form': new_reaction_form
    })


# answer form in topic detail
def new_answer(request, id_category=0, id_topic=0):
    if request.method == 'POST':
        new_answer_post = AnswerOnPost(request.POST)
        if new_answer_post.is_valid():
            text = new_answer_post.cleaned_data.get("text")
            if text:
                answer = Answer(text=text, topic_id=id_topic, x_user_id=request.user.id)
                answer.save()

    return AnswerOnPost()


# delete function for move answer or post to history
def delete_answer(request, id_answer):
    if request.method == 'GET':
        answer = Answer.objects.get(id_answer=id_answer)
        answer.deleted = True
        answer.save()
        messages.success(request, 'Smazání proběhlo úspěšně.')
        return redirect(reverse('topic', kwargs={
            "id_category": answer.topic.category_id,
            "id_topic": answer.topic_id,
        }))


# called from ajax
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


# called from ajax
def new_reaction(request, id_answer=0):
    id_answer = int(id_answer)
    if request.method == 'POST' and id_answer != 0:
        new_reaction = NewReaction(request.POST)
        if new_reaction.is_valid():
            text = new_reaction.cleaned_data.get("text")
            answer = Answer.objects.get(id_answer=id_answer)
            if text and answer:
                record = Reaction(text=text, answer=answer, x_user_id=request.user.id)
                record.save()
                return redirect(reverse('topic', kwargs={
                    "id_category": answer.topic.category_id,
                    "id_topic": answer.topic_id,
                }))
            return NewReaction()
    else:
        return NewReaction()
