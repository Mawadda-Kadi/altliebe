from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='users/static/images/profile_default_image.png')
    email = models.EmailField(default='', null=True, blank=True)
    about_me = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()