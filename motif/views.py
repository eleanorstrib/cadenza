from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml
from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from emoji import Emoji

def index(request):
    return(HttpResponse("index page!"))

@twilio_view
def sms(request):
    user_msg = request.POST.get('Body', '')
    msg = user_msg
    r = twiml.Response()
    r.message(msg)
    return r
