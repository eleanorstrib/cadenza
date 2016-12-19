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
    um_text_only = user_msg[1:-1] # removes ::
    if um_text_only in Emoji.names():
        msg = "Thanks!  We recorded your message: %s" % user_msg
    else:
        msg = "Oops - your input must be a single emoji. You typed %s and the text only is %s" % (user_msg, um_text_only)
    r = twiml.Response()
    r.message(msg)
    return r
