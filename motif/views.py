from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml
from twilio.twiml import Response

def index(request):
    return(HttpResponse("index page!"))

def sms(request):
    r = Response()
    r.message("hello there!")
    return r
