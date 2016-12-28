from django import forms
from django.contrib.auth.models import User
from .models import UserModel
from phonenumber_field.modelfields import PhoneNumberField


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = UserModel()
#         fields = ('username', 'email', 'password', 'mobile_phone')
