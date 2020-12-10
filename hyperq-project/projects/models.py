from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Project(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="posts")
    title = models.CharField(max_length=75)
        
    # metadata    
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    dt_create = models.DateTimeField(default=timezone.now)
    dt_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-dt_create']


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)        
        # set post slug
        self.slug = self.get_slug()
        super().save(update_fields=['slug'])

    def get_slug(self):
        return f'{self.id}-{slugify(self.title)}'