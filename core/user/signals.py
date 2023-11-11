from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile_user(sender, **kwargs):
    if kwargs.get("created"):
        user_instance = kwargs.get("instance")
        Profile.objects.create(user=user_instance)
