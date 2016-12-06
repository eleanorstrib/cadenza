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
    if user_msg == Emoji.replace(:smile:)
        msg = "get happy!"
    else:
        msg = "No go"
    r = twiml.Response()
    r.message(msg)
    return r
