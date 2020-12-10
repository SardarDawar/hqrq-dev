from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from .vars import PROJ_STAGE_CHOICES, PROJ_STAGE_DEFAULT, PROJ_STATUS_CHOICES, PROJ_STATUS_DEFAULT, PROJ_TYPE_CHOICES, PROJ_SUBTYPE_CHOICES, PROJ_SUBTYPE_CHOICES_SEL

class Project(models.Model):

    # project stages

    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="projects")
    title = models.CharField(max_length=500)
    
    # doc attributes
    doc_type = models.CharField(max_length=25, choices=PROJ_TYPE_CHOICES)
    doc_subtype = models.CharField(max_length=25, choices=PROJ_SUBTYPE_CHOICES)

    stage = models.CharField(max_length=25, choices=PROJ_STAGE_CHOICES, default=PROJ_STAGE_DEFAULT)
    status = models.CharField(max_length=25, choices=PROJ_STATUS_CHOICES, default=PROJ_STATUS_DEFAULT)


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

    def get_possible_subtypes(self):
        return PROJ_SUBTYPE_CHOICES_SEL[self.doc_type]