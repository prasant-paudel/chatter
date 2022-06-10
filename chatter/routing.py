import os

from message.middlewares import WebSocketJWTAuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from message import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatter.settings')


application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': WebSocketJWTAuthMiddleware(URLRouter(routing.message_urlpatterns)),
    }
)
