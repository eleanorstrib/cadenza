from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sms/$', views.sms, name='sms'),
    url(r'^message/$', 'django_twilio.views.message', {
        'message': 'Thanks for the SMS. Talk to you soon!',
    }),
]
