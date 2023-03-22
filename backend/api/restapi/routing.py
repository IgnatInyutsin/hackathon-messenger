# chat/routing.py
from django.urls import path
from restapi.app.consumers import *

websocket_urlpatterns = [
    path("ws/chat/(?P<chat_id>\w+)/$", ChatConsumer.as_asgi())
]