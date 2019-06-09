# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'forum_base.html', {})