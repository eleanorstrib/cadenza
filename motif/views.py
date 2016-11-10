from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return(HttpResponse("index page!"))

@twilio_view
def sms_test(request):
    name = request.POST.get('Body', '')
    msg = "hi %s!!!" % (name)
    r = Response()
    r.message(msg)
    return r
