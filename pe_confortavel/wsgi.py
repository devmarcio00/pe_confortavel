"""
Configuração WSGI para o projeto pe_confortavel.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pe_confortavel.settings')

application = get_wsgi_application()
