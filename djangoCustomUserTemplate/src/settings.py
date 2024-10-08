"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hx84i_k8zx4^5i%&tj)wmuj4m1^_%8uy=+4^i6dzu*p84%(dj3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    ### third-party
    'crispy_forms',

    # django-allauth needs this
    'django.contrib.sites', 
    # below are everything all-auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to allauth to enable:
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',
    # add more if you wish to

    ### defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ### customs
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware', # for django-allauth
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")     # where we want django to save uploaded files
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



################################################### ALL OTHER ADDITIONAL CUSTOM SETTINGS
AUTH_USER_MODEL = 'users.User' # for the project to use the custom User we created instead of the default
CRISPY_TEMPLATE_PACK = 'bootstrap4' # for the css of crispy forms
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# TO USE THESE VARIABLES BELOW, USE ENVIRONMENT VARIABLES TO HIDE SENSITIVE INFO
# CHECK CoreyMs' Django TUTORIAL # 12 -- 14:20
EMAIL_HOST_USER = os.environ.get('ADMIN_EMAIL_UN') # var for email username
EMAIL_HOST_PASSWORD = os.environ.get('ADMIN_EMAIL_PW') # var for email pw
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER # for email-sending pw-reset requests
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # or only your domain name if you have your own mail server
EMAIL_PORT = 587 #587
EMAIL_USE_TLS = True





# django-allauth needs this
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Provider specific settings for django-allauth
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': os.environ.get('GAUTH_CLIENTID'), # '960711795493-9vsgskaeg1qk3nc74qp27s9e7uoejitq.apps.googleusercontent.com'
            'secret': os.environ.get('GAUTH_SECRET'),      # '0-tHwlg4jvax1jt7p-JnvBmj'
            'key': ''
        }
    }
}
### some more django-allauth settings. see https://docs.allauth.org/en/latest/account/configuration.html
'''
    will try to remove the custom user authentication views after successfully implementing these
'''
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_PASSWORD_MIN_LENGTH = 8

