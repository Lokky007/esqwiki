# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from questions.models import questions
from forms import QuestionsNewPost


def index(request):
    if request.method == 'POST':
        form = QuestionsNewPost(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            record = questions(text=text, x_user_id=1)
            record.save()

    question_new_post = QuestionsNewPost()
    records = questions.objects.filter(deleted=0).order_by('-x_created')
    return render(request, 'questions_base.html',
                  {
                      'questions_records': records,
                      'questions_new_post': question_new_post
                  })


