from django.shortcuts import render
from .forms import UserForm, ProfileForm
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponse('form valid!')
        else:
            return HttpResponse('form not valid')
    else:
        return HttpResponse('request method was GET')

    return render(request, 'signup/index.html', {'user_form': user_form, 'profile_form': profile_form})
