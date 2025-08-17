from django.urls import path, re_path
from .consumers import MySyncConsumer

websocket_urlpatterns = [
    path('ws/sc/', MySyncConsumer.as_asgi()),
    # re_path(r"ws/sc/(?P<name>\w+)/$", MySyncConsumer.as_asgi()),
    # path('ws/ac/', MyAsyncConsumer.as_asgi()),
]
