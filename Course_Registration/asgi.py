"""
ASGI config for Course_Registration project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Course_Registration.settings')
django.setup()
from channels.auth import AuthMiddlewareStack

application = get_asgi_application()


# import os
# import django
# from channels.routing import ProtocolTypeRouter , URLRouter
# from django.core.asgi import get_asgi_application
# from django.urls import path
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Course_Registration.settings')
# django.setup()
# from channels.auth import AuthMiddlewareStack
# from Notification.routing import websocket_urlpatterns

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack( 
#         URLRouter(
#             websocket_urlpatterns
#             ),
#     )
# })
                            