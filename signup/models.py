from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_phone = PhoneNumberField()
    tracker_name = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_profile (sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile (sender, instance, **kwargs):
    instance.profile.save()
