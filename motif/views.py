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
    if msg = :smile:
        msg = user_msg
    else:
        msg = "hi there"
    r = twiml.Response()
    r.message(msg)
    return r
