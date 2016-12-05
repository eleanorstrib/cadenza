from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml
from twilio.twiml import Response
from django_twilio.decorators import twilio_view
import emoji

def index(request):
    return(HttpResponse("index page!"))

@twilio_view
def sms(request):
    user_msg = str(request.POST.get('Body', ''))
    msg = unicode(user_msg, 'utf-8')
    r = twiml.Response()
    r.message(msg)
    return r
