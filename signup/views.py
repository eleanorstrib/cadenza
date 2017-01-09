from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CadenzaUser
from .forms import CadenzaUserForm
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        form = CadenzaUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success!")
    else:
        form = CadenzaUserForm()

    return render(request, 'signup/index.html',{'form': form})
