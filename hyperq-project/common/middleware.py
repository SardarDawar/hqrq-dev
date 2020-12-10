from django.conf import settings
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.models import Site
import datetime as dt
import json
from common.models import Setting

class AppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        self.site = Site.objects.get_current()
        try:
            self.site_settings = self.site.settings
        except AttributeError:
            self.site_settings = None

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        # if not request.path.startswith('/admin/'):

        response = self.get_response(request)
        
        # Code to be executed for each request/response after
        # the view is called.
        return response