"""
ASGI config for Supermarket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application


#base_settings
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Supermarket.settings')

#develop_seetings(开发环境)
profile = os.environ.get('default_profile','develop_settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Supermarket.Settings.%s' % profile)

application = get_asgi_application()
