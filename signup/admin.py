from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from signup.models import CadenzaUser

# class ProfileInline(admin.StackedInline):
#     model=Profile
#     can_delete = False
#     verbose_name_plural = "user profile"
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline, )
#
# admin.site.unregister(User)
admin.site.register(CadenzaUser)
