import os
from django.contrib.auth.models import User
from django.db import models
from common.storage import OverwriteStorage
from common.utils import resizeImage
from django.conf import settings

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

BASE_PATH = "users"
PROFILE_PICTURES_PATH = os.path.join(BASE_PATH, 'profile_pictures')

def profileImageSavePath(instance, filename):
    return os.path.join(PROFILE_PICTURES_PATH, f'{instance.user.username}'+os.path.splitext(filename)[1])


# users (FOLDER)
# -- user1 (FOLDER)
# -- -- icon.png

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    image = models.ImageField(null=True, blank=True, storage=OverwriteStorage(), upload_to=profileImageSavePath)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        name = self.get_full_name()
        return f'{self.email} [{name}]' if name else self.email 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # resize image
        if self.image:
            resizeImage(self.image.path, 300, 300)
