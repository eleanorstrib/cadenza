from django.shortcuts import render

def index(request):
    # form = UserForm()
    return render(request, 'signup/index.html', {})
