"""Django per environment settings loading."""
import importlib
import os

enviroment_settings = importlib.import_module('PROJECT.config.{}'.format(os.getenv('ENVIRONMENT')))

for setting in dir(enviroment_settings):
    if setting == setting.upper():
        locals()[setting] = getattr(enviroment_settings, setting)
