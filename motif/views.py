from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml
from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from emoji import Emoji

def index(request):
    return render(request, 'motif/index.html', {})

@twilio_view
def sms(request):
    user_msg = request.POST.get('Body', '')
    if user_msg in Emoji.names():
        msg = "Thanks!  We recorded your message: %s" % user_msg
    else:
        msg = "Oops - your input must be a single emoji."
    r = twiml.Response()
    r.message(msg)
    return r
