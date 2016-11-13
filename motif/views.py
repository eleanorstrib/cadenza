from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml
from twilio.twiml import Response
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return(HttpResponse("index page!"))

@csrf_exempt
def sms(request):
    r = Response()
    r.message("hello there!")
    return r
