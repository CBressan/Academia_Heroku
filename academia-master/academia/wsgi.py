"""
WSGI config for academia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academia.settings')

application = Cling(get_wsgi_application())
'''toda requisição q chegar, o Cling irá verificar primeiro se é um arquivo estático, e se não for, entrega por django, se for, 
  o Cling cuidará disso'''
