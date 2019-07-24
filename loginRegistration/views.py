# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp)) +  six.text_type(user.is_active)

# Login - check and redirect
def Login(request):
    loginForm = UserLoginForm(request.POST or None)
    if loginForm.is_valid():
        username = loginForm.cleaned_data.get("username")
        password = loginForm.cleaned_data.get("passsword")
        user = authenticate(username=username, password=password)
        print user, username, password
        login(request, user)
        if request.user.is_authenticated():
            return redirect('/main/')

    return render(request, 'extension/login.html', {"loginForm": loginForm})


# Register - check data and if correct, redirect.
def Register(request):
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

    return render(request, 'extension/registration.html', {"form": form})


def RegistrationEmail(request, user, password):
    subject = 'Registrace na ESQWiki'

    current_site = get_current_site(request)
    account_activation_token = AccountActivationTokenGenerator()

    html_message = render_to_string('emailRegistration.html', {
                            'user': user,
                            'password': password,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode("utf-8"),
                            'token': account_activation_token.make_token(user),
    })
    # send activation link to the user
    user.email_user(subject=subject, message=html_message)


# Logout function for destroy relation
def Logout (request):
    logout(request)
    return render(request, 'extension/logout.html')


def activate(request, uidb64, token):
    try:
        account_activation_token = AccountActivationTokenGenerator()

        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/login/')
    else:
        return HttpResponse('Aktivace uctu probehla uspesne.')
