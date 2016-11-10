from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml
from django_twilio.decorators import twilio_view
from twilio.twiml import Response

def index(request):
    return(HttpResponse("index page!"))

@twilio_view
def sms_test(request):
    r = twiml.Response()
    r.message("hello there!")
    return r
