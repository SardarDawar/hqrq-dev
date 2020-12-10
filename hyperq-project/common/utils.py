from PIL import Image
import threading
from threading import Thread
from django.core.mail import EmailMessage
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.sites.models import Site
from django.core.exceptions import AppRegistryNotReady

def resizeImage(path, x, y):
    img = Image.open(path)
    if img.height > x or img.width > y:
        output_size = (x, y)
        img.thumbnail(output_size)
        img.save(path)


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, to=self.recipient_list)
        msg.content_subtype = "html"
        msg.send()

def send_html_email_async(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()


class CustomUsernameValidator(UnicodeUsernameValidator):
    """Allows \."""
    # message = 'Enter a valid entrypoint. This value may contain only letters, numbers, and @/./+/-/_ characters.'
    message = 'Username may contain only letters, numbers, and ./-/_ characters.'

validator_username = CustomUsernameValidator()

class CustomNameValidator(UnicodeUsernameValidator):
    """Allows \."""
    # message = 'Enter a valid entrypoint. This value may contain only letters, numbers, and @/./+/-/_ characters.'
    message = "Name may contain only letters, numbers, and '-' character."

validator_name = CustomNameValidator()





class UtilitySiteSettings():

    def __init__(self):
        try:
            site = Site.objects.get_current()
            self.site_settings = site.settings
        except (AttributeError, KeyError, AppRegistryNotReady):
            # print('Warning! Site settings have not been initialized.')
            self.site_settings = None
        except:
            # print('Warning! Site settings have not been initialized.')
            self.site_settings = None

    def verifySettingsLoaded(self):
        if self.site_settings is None:
            try:
                site = Site.objects.get_current()
                self.site_settings = site.settings
                return True
            except (AttributeError, KeyError, AppRegistryNotReady):
                # print('Warning! Site settings have not been initialized.')
                return False
            except:
                return False
        return True

uSiteSettings = UtilitySiteSettings()