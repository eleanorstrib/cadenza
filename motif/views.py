from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml
from twilio.twiml import Response
from django_twilio.decorators import twilio_view

@twilio_view
def index(request):
    r = twilio.twiml.Response()
    r.message("hello there!")
    return r
    # return(HttpResponse("index page!"))
#
# @twilio_view
# def sms(request):
