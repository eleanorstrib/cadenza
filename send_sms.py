import os
from twilio.rest import TwilioRestClient
import twilio.twiml

tw_sid = os.environ['TWILIO_ACCOUNT_SID']
tw_auth = os.environ['TWILIO_AUTH_TOKEN']
tw_phone = os.environ['TWILIO_DEFAULT_CALLERID']
my_phone = os.environ['TWILIO_TEST_PHONE']

client = TwilioRestClient(tw_sid, tw_auth)

message = client.messages.create(to=my_phone, from_=tw_phone, body="hello Eleanor")
