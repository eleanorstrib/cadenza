from django import forms
from django.contrib.auth.models import User
from .models import User, Profile
from phonenumber_field.modelfields import PhoneNumberField


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('mobile_phone', 'tracker_name')
