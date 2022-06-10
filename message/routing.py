from django.urls import re_path

from . import consumers

message_urlpatterns = [
    re_path(r'msg/', consumers.ChatConsumer.as_asgi()),
]