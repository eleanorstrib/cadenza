from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print(profile_form)
        if user_form.is_valid():
            print("user form valid")
        else:
            print("user form didn't work", user_form)
        if profile_form.is_valid():
            user_form.save()
            profile_form.user = request.user
            profile_form.save()
            print("profile form valid")
        else:
            return HttpResponse('form not valid')
    else:
        user_form = UserForm
        profile_form = ProfileForm

    return render(request, 'signup/index.html',{'user_form': user_form, 'profile_form': profile_form})
