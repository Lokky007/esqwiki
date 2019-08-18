# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def user_detail(request, id_user):
    """
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("user_login")
        password = form.cleaned_data.get("user_pass")
        fname = form.cleaned_data.get("user_name")
        lname = form.cleaned_data.get("user_last_name")
        email = form.cleaned_data.get("user_email")

        newUser = User.objects.create_user(username, email, password, last_name=lname, first_name=fname)

        RegistrationEmail(request, newUser, password)

        return render(request, 'extension/registrationSuccess.html', {"username": username})
    """

    return render(request, 'user_detail.html', {})


def guild_detail(request, id_guild):
    """

    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("user_login")
        password = form.cleaned_data.get("user_pass")
        fname = form.cleaned_data.get("user_name")
        lname = form.cleaned_data.get("user_last_name")
        email = form.cleaned_data.get("user_email")

        newUser = User.objects.create_user(username, email, password, last_name=lname, first_name=fname)

        RegistrationEmail(request, newUser, password)

        return render(request, 'extension/registrationSuccess.html', {"username": username})
    """

    return render(request, 'guild_detail.html', {})
