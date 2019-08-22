# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from questions.models import questions
from forms import QuestionsNewPost
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


def index(request):
    if request.method == 'POST':
        form = QuestionsNewPost(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            record = questions(text=text, x_user_id=request.user.id)
            record.save()

    question_new_post = QuestionsNewPost()
    records = questions.objects.filter(deleted=0).order_by('-x_created')
    return render(request, 'questions_base.html',
                  {
                      'questions_records': records,
                      'questions_new_post': question_new_post
                  })

@csrf_exempt
def right_answer(request):
    answer_id = int(request.POST['answer_id'])

    record_questions = questions.objects.filter(id_question_post=answer_id)
    record_questions.update(is_answer=True)

    record_main = questions.objects.filter(id_question_post_parent=record_questions[0].id_question_post)
    record_main.update(is_resolved=True)
    return HttpResponse(json.dumps("ok"), content_type="application/json")
