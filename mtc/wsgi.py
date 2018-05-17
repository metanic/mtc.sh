""" Entry-point for WSGI applications. """

import os

from django.core import wsgi

import mtc

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtc.settings.production')

application = wsgi.get_wsgi_application()