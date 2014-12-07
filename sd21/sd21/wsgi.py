"""
WSGI config for sd21 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

sys.path.append('/home/y-sato/workspace_env1/sd21')
sys.path.append('/home/y-sato/workspace_env1/sd21/sd21')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sd21.settings")

site.addsitedir('/home/y-sato/.virtualenvs/env1/lib/python3.4/site-packages')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
