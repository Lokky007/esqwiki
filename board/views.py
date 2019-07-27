# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from board.models import posts
from questions.views import index as questions_form
from questions.forms import QuestionsNewPost
from questions.models import questions
from forms import BuySellPost


def index(request):
    if request.method == 'POST':
        buy_sell_form_post = BuySellPost(request.POST)
        if buy_sell_form_post.is_valid() and request.POST.get('buySell'):
            text = buy_sell_form_post.cleaned_data.get("text")
            if text:
                record = posts(text=text, x_user_id=request.user.id)
                record.save()

        # call old structure of questions
        if request.POST.get('question'):
            questions_form(request)

    buy_sell_new_post = BuySellPost()
    help_new_post = QuestionsNewPost()

    return render(request, 'board_base.html',
                  {
                      'board_records': prepare_data_questions_block(),# data
                      'sellBuy_records': prepare_data_sell_buy_block(),# data
                      'user': request.user,
                      'help_new_post': help_new_post,# form
                      'sell_buy_new_post': buy_sell_new_post # form
                  })


def prepare_data_questions_block():
    question_array = []
    records_questions = questions.objects.filter(deleted=0, id_question_post_parent=None).order_by('-x_created')
    for record in records_questions:
        answer_array = []
        answers = questions.objects.filter(deleted=0, id_question_post_parent=record.id_question_post).order_by(
            '-x_created')
        for answer in answers:
            answer_array.append(answer)

        question_array.append([record, answer_array])

    return question_array


def prepare_data_sell_buy_block():
    sell_buy_array = []
    records_posts = posts.objects.filter(deleted=0, id_board_post_parent=None).order_by('-x_created')
    for record in records_posts:
        sell_buy_comments_array = []
        sell_buy = posts.objects.filter(deleted=0, id_board_post_parent=record.id_board_post).order_by('-x_created')
        for item in sell_buy:
            sell_buy_comments_array.append(item)

        sell_buy_array.append([record, sell_buy_comments_array])
    return sell_buy_array


def delete_post(request, id_post):
    if request.method == 'GET':
        t = posts.objects.get(id_board_post=id_post)
        t.deleted = 1
        t.save()
        messages.success(request, 'Smazání proběhlo úspěšně.')
    return redirect('/board/')


def answer(request, id_post):
    if request.method == 'POST':
        text = request.POST['text']
        if text:
            record = posts(text=text, id_board_post_parent=id_post, x_user_id=request.user.id)
            record.save()
    return redirect('/board/')
