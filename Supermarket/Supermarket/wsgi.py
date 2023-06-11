"""
WSGI config for Supermarket project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#base_settings
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Supermarket.settings')

#develop_seetings(开发环境)

profile = os.environ.get('default_profile','develop_settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Supermarket.Settings.%s' % profile)

application = get_wsgi_application()
