"""
ASGI config for django_fastapi_integration project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from myapp.api import app as fastapi_app
from fastapi.responses import HTMLResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_fastapi_integration.settings')

django_application = get_asgi_application()

async def application(scope, receive, send):
    if scope['type'] == 'http':
        if scope['path'].startswith('/api'):
            await fastapi_app(scope, receive, send)
        else:
            await django_application(scope, receive, send)
    else:
        await django_application(scope, receive, send)
