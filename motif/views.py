from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return(HttpResponse("index page!"))

@twilio_view
def sms_test(request):
    r=Response()
    r.message("thanks for your text :)")
    return r
