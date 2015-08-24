"""Base django settings file."""

import os

########################################################################
#
# Environmental variables
#
# List all your ENV VARIABLES in one place to quickly remember which are
# used in your project.
#
########################################################################

# Optional variables are set here.
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
DEBUG = bool(env_vars['DEBUG'])

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

########################################################################
#
# Apps settings
#
########################################################################

A_REQUIRED_APP_SETTING = env_vars['A_VARIABLE_WITH_A_VALUE']
if env_vars['AN_OPTIONAL_VARIABLE']:
    AN_OPTIONAL_APP_SETTING = env_vars['AN_OPTIONAL_VARIABLE']
