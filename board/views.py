from django.shortcuts import render
from django.http import HttpResponse
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

def delete_post(request):
    if request.method == 'POST':
        t = posts.objects.get(id=1)
        t.value = 999  # change field
        t.save()