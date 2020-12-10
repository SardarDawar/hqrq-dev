import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# import secret key
try:
    from common.secrets import HQ_SECRET_KEY
except (ModuleNotFoundError, ImportError):
    HQ_SECRET_KEY = get_random_secret_key()
    # store this key to new secrets file
    secrets_file = os.path.join(BASE_DIR, 'common', 'secrets.py')
    secrets_file_flag = 'a' if os.path.exists(secrets_file) else 'w'
    with open(secrets_file, secrets_file_flag) as secrets_fp:
        secrets_fp.write(f"\nHQ_SECRET_KEY = '{HQ_SECRET_KEY}'\n")

# import smtp credentials
try:
    from common.secrets import HQ_EMAIL_HOST_USER, HQ_EMAIL_HOST_PASSWORD
except (ModuleNotFoundError, ImportError):
    HQ_EMAIL_HOST_USER = ''
    HQ_EMAIL_HOST_PASSWORD = ''

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = HQ_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # imported apps
    'django_cleanup.apps.CleanupConfig',
    'django.contrib.humanize',
    # my apps
    'common.apps.CommonConfig',
    'users.apps.UsersConfig',
    'projects.apps.ProjectsConfig',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # custom middleware
    # 'common.middleware.AppMiddleware',
    ##################################
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hyperq.urls'
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [            
            os.path.join('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # custom context processor
                'common.context_processors.site_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'hyperq.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join('static'), )

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Login Redirect & URL

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# EMAIL Backend Configuration

EMAIL_BACKEND =         'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST =            'smtp.gmail.com'
EMAIL_PORT =            587
EMAIL_USE_TLS =         True
EMAIL_HOST_USER =       HQ_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD =   HQ_EMAIL_HOST_PASSWORD