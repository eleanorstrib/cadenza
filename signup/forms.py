from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CadenzaUser
from phonenumber_field.modelfields import PhoneNumberField


class CadenzaUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CadenzaUser
        fields = UserCreationForm.Meta.fields + ('email', 'mobile', 'password', 'tracker_name')
