from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return(HttpResponse("index page!"))

def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    print("sending")
    return str(resp)
