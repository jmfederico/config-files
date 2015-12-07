"""Base django settings file based on Django 1.9 settings."""

import os

########################################################################
#
# Environmental variables
#
# List all your ENV VARIABLES in one place to quickly remember which are
# used in your project.
#
########################################################################

# Required variables are set here.
# Use dictionary-like syntax to force error when not present.
env_vars = {
    'A_REQUIRED_VARIABLE': os.environ['A_REQUIRED_VARIABLE'],

    'BASE_HOST': os.environ['BASE_HOST'],
    'SECRET_KEY': os.environ['SECRET_KEY'],
}
# Use this syntax for the ones you just need to check for existance,
# but won't actually use on the settings file.
os.environ['ANOTHER_REQUIRED_VAR']

# Optional variables are set here. Project can run without it.
# use os.getenv() instead of dictionary-like syntax.
env_vars.update({
    'AN_OPTIONAL_VARIABLE': os.getenv('AN_OPTIONAL_VARIABLE', None),

    'ALLOWED_HOSTS': os.getenv('ALLOWED_HOSTS', '').split(),
    'DEBUG': os.getenv('DEBUG', False),
})

########################################################################
#
# Base Non-Django settings
#
# Settings that you share/use in multiple places across your project.
#
########################################################################

BASE_HOST = env_vars['BASE_HOST']

########################################################################
#
# Debug settings
#
########################################################################

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_vars['DEBUG'] in [True, "1", "True"]

########################################################################
#
# Base Django settings
#
# Settings from the original django settings.py file are set here.
#
########################################################################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_vars['SECRET_KEY']

ALLOWED_HOSTS = [BASE_HOST] + env_vars['ALLOWED_HOSTS']
ROOT_URLCONF = 'PROJECTNAME.urls'
WSGI_APPLICATION = 'PROJECTNAME.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'collect-static/')
STATIC_URL = '/st/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

########################################################################
#
# Apps settings
#
########################################################################

A_REQUIRED_APP_SETTING = env_vars['A_REQUIRED_VARIABLE']
if env_vars['AN_OPTIONAL_VARIABLE']:
    AN_OPTIONAL_APP_SETTING = env_vars['AN_OPTIONAL_VARIABLE']
