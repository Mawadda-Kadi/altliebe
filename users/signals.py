from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            Profile.objects.get_or_create(user=instance)
        except IntegrityError:
            # Handle the case where the profile already exists
            # Log the error, send a notification, or simply pass
            pass