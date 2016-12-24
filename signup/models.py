from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_phone  = PhoneNumberField()
