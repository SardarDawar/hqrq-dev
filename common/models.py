from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

class Setting(models.Model):

    # site-url can be set in corresponding Site-table entry
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name='settings', default=settings.SITE_ID)

    # app basic-info
    app_name = models.CharField(max_length=200, default='Hyper Questions', verbose_name="App Name")
    tagline = models.CharField(max_length=200, blank=True, null=True, verbose_name="Tagline")
    about = models.CharField(max_length=2500, blank=True, null=True, verbose_name="About")
    contact_address = models.CharField(max_length=500, blank=True, null=True)
    contact_tel = models.CharField(max_length=25, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    # app social-links
    social_link_facebook = models.CharField(max_length=1000, blank=True, null=True) 
    social_link_twitter = models.CharField(max_length=1000, blank=True, null=True) 
    social_link_instagram = models.CharField(max_length=1000, blank=True, null=True) 

    def __str__(self):
        return f'Settings for site {self.site.domain}'
