import os
from django.contrib.auth.models import User
from django.db import models
from common.storage import OverwriteStorage
from common.utils import resizeImage

BASE_PATH = "users"
PROFILE_PICTURES_PATH = os.path.join(BASE_PATH, 'profile_pictures')

def profileImageSavePath(instance, filename):
    return os.path.join(PROFILE_PICTURES_PATH, f'{instance.user.username}'+os.path.splitext(filename)[1])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, storage=OverwriteStorage(), upload_to=profileImageSavePath)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # resize image
        if self.image:
            resizeImage(self.image.path, 300, 300)

# users (FOLDER)
# -- user1 (FOLDER)
# -- -- icon.png
