from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml
from twilio.twiml import Response
from django_twilio.decorators import twilio_view

def index(request):
    return(HttpResponse("index page!"))

@twilio_view
def sms(request):
    user_msg = request.POST.get('Body', '')
    if user_msg == ":)":
        msg = "yay you're ", user_msg
    else:
        msg = "not happy?"
    r = twiml.Response()
    r.message(msg)
    return r
