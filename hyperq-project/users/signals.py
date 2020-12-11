from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.conf import settings

@receiver(post_save, sender=User)
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        if settings.DEBUG:
            Profile.objects.create(user=instance, email_verified=True)
        else:
            Profile.objects.create(user=instance)

# not necessary to save the profile each time (for now)
# @receiver(post_save, sender=User)
# def SaveProfile(sender, instance, **kwargs):
#     instance.profile.save()

# @receiver(user_logged_out)
# def on_user_logged_out(sender, request, **kwargs):
#     messages.add_message(request, messages.WARNING, 'You are now Logged Out')

# @receiver(user_logged_in)
# def on_user_logged_in(sender, request, **kwargs):
#     messages.add_message(request, messages.SUCCESS, 'Successfully Logged In')
