# chat/routing.py
from django.urls import path
from restapi.app.consumers import *

websocket_urlpatterns = [
    path('ws/chat/<chat_id>/', ChatConsumer.as_asgi())
]