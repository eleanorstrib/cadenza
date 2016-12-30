from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            print("user form valid")
        else:
            print(user_form)
        if profile_form.is_valid():
            # profile_form.save()
            print("profile form valid")
            return HttpResponse('form valid!')
        else:
            return HttpResponse('form not valid')
    else:
        user_form = UserForm
        profile_form = ProfileForm

    return render(request, 'signup/index.html',
        {'user_form': user_form, 'profile_form': profile_form})
