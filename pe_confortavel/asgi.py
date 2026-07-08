"""
Configuração ASGI para o projeto pe_confortavel.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pe_confortavel.settings')

application = get_asgi_application()
