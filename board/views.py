# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from board.models import posts
from forms import BoardNewPost


def index(request):
    if request.method == 'POST':
        form = BoardNewPost(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            record = posts(text=text, x_user_id=1)
            record.save()

    board_new_post = BoardNewPost()
    records = posts.objects.filter(deleted=0).order_by('-x_created')
    return render(request, 'board_base.html',
                  {
                      'board_records': records,
                      'board_new_post': board_new_post
                  })


def delete_post(request, id_post):
    if request.method == 'GET':
        t = posts.objects.get(id_board_post=id_post)
        t.deleted = 1
        t.save()
        messages.success(request, 'Smazání proběhlo úspěšně.')
    return redirect('/board/')
