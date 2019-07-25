# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from board.models import posts
from forms import BoardNewPost


def index(request):
    if request.method == 'POST':
        formPost = BoardNewPost(request.POST)
        if formPost.is_valid():
            text = formPost.cleaned_data.get("text")
            if text:
                record = posts(text=text, x_user_id=request.user.id)
                record.save()

    board_new_post = BoardNewPost()
    postArray= []
    records = posts.objects.filter(deleted=0, id_board_post_parent=None).order_by('-x_created')
    for record in records:
        answerArray = []
        answers = posts.objects.filter(deleted=0, id_board_post_parent=record.id_board_post).order_by('-x_created')
        for answer in answers:
            answerArray.append(answer)

        postArray.append([record, answerArray])


    return render(request, 'board_base.html',
                  {
                      'board_records': postArray,
                      'user': request.user,
                      'board_new_post': board_new_post
                  })


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
