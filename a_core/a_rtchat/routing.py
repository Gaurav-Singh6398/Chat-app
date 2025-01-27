from django.urls import path
from .consumers import *  # Make sure to import the specific consumer

websocket_urlpatterns = [
    path("ws/chatroom/<chatroom_name>", ChatroomConsumer.as_asgi()),  # Fixed the URL and the path argument
]



