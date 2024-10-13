from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
# Credit: https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL
# -osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9


# Automatically create a Profile when a new User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Save the Profile whenever the User is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
