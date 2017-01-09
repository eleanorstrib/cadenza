from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_info = user_form.save()
            user_id = user_info.id
            profile_form.save()
            return HttpResponse("success!")
        else:
            return HttpResponse("there was a problem saving the form")
    else:
        user_form = UserForm
        profile_form = ProfileForm

    return render(request, 'signup/index.html',{'user_form': user_form, 'profile_form': profile_form})
