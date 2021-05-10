# To create profile when a user is registered.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)   # when signal is received, it creates a profile object.
def create_profile(sender, instance, created, **kwargs):   # kwargs accepts any additional keywords.
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)   # when signal is received, it saves a profile object.
def save_profile(sender, instance, **kwargs):
    instance.profile.save()