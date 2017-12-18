from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm


@login_required
def index(request):
    return HttpResponse("Hello")


def login(request):
    return HttpResponse("a")


def register_user(request):
    user_form = UserForm(prefix='user')
    user_profile_form = UserProfileForm(prefix='profile')
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='user')
        user_profile_form = UserProfileForm(request.POST, prefix='profile')
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            return redirect("/")
    return render(
        request,
        'registration.html',
        {
            'user_form': user_form,
            'user_profile_form': user_profile_form,
        }
    )
