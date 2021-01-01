from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from .utils import setupProjectBaseProperties
from .vars import ( PROJ_STAGE_CHOICES, PROJ_STAGE_DEFAULT, PROJ_STATUS_CHOICES, PROJ_STATUS_DEFAULT, 
                    PROJ_TYPE_CHOICES, PROJ_TYPE_DEFAULT, PROJ_SUBTYPE_CHOICES, PROJ_SUBTYPE_CHOICES_SEL, PROJ_SUBTYPE_DEFAULT,
                    PROJ_DOCSIZE_CHOICES, PROJ_DOCSIZE_DEFAULT, 
                    PROJ_TOPIC_CHOICES, PROJ_TOPIC_DEFAULT, )
from .content import PROJ_TYPE_SVGS, getExpressedTerm, getUnexpressedTerm
from django.conf import settings

class Project(models.Model):

    # project attributes
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="projects")
    title = models.CharField(max_length=500)
    
    # doc attributes
    doc_type = models.CharField(max_length=25, choices=PROJ_TYPE_CHOICES, null=True)
    doc_subtype = models.CharField(max_length=25, choices=PROJ_SUBTYPE_CHOICES, null=True)
    doc_len = models.CharField(max_length=25, choices=PROJ_DOCSIZE_CHOICES, null=True)
    doc_topic = models.CharField(max_length=25, choices=PROJ_TOPIC_CHOICES, null=True)

    # project state
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
    
    def __str__(self):
        return f'[{self.creator.email}] {self.title}'

    def setupBaseProperties(self, update_stage=True):
        setupProjectBaseProperties(self, update_stage=True)

    def getProjectTypeSVG(self):
        return PROJ_TYPE_SVGS[self.doc_type]

class Property(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="props")
    name = models.CharField(max_length=25)
    response = models.CharField(max_length=1000, null=True)
    response_exp = models.CharField(max_length=1100, null=True)

    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-project__dt_create', 'name']
    
    def __str__(self):
        return f'[{self.project.title}] {self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # store response_exp if not present (when response given for first time)
        print(self.response)
        if self.response and not self.response_exp: 
            self.response_exp = getExpressedTerm(self.name, self.response)
            self.save(update_fields=["response_exp"])

    def updateUnexpressedResponse(self, exp_resp=None):
        if not self.response_exp and not exp_resp: return
        update_fields = []
        if exp_resp:
            self.response_exp = exp_resp
            update_fields.append("response_exp")
        self.response = getUnexpressedTerm(self.response_exp)
        update_fields.append("response")
        self.save(update_fields=update_fields)
    
    def updateExpressedResponse(self, resp=None):
        if not self.response and not resp: return
        update_fields = []
        if resp:
            self.response = resp
            update_fields.append("response")
        self.response_exp = getExpressedTerm(self.name, self.response)
        update_fields.append("response_exp")
        self.save(update_fields=update_fields)