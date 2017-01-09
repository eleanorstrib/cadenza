from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# from django.utils.translation import ugettext_lazy as _

class CadenzaUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    mobile = PhoneNumberField()
    tracker_name = models.CharField(
                                max_length=50,
                                default='My tracker',
                                blank=True
                                )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'mobile']
