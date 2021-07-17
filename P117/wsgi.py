"""
WSGI config for P117 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/opt/bitnami/projects/P117')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/projects/P117/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "P117.settings")
application = get_wsgi_application()
