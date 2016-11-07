import os
from twilio.rest import TwilioRestClient
import twilio.twiml

tw_sid = os.environ['TW_AUTH_ID']
tw_auth = os.environ['TW_AUTH_TK']
tw_phone = os.environ['TW_PHONE_NO']
my_phone = os.environ['TS_PHONE_NO']

client = TwilioRestClient(tw_sid, tw_auth)

message = client.messages.create(to=my_phone, from_=tw_phone, body="hello Eleanor")
