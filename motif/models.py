from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class Person(models.Model):
    user = (models.OneToOneField(User, on_delete=models.CASCADE))
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.username

class TextMsg(models.Model):
    user = models.ForeignKey(User)
    msg_from = PhoneNumberField()
    msg_date = models.DateTimeField()
    msg_body = models.CharField(max_length=280)

    def __str__(self):
        return self.user
