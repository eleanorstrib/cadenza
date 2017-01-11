from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from signup.models import CadenzaUser

admin.site.register(CadenzaUser)
