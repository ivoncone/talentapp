from django.urls import path
from channels.routing import ProtocolTypeRouter

from chat import consumers

"""application = ProtocolTypeRouter({
	path('ws/message/', consumers.SendMessageConsumer.as_asgi(),)
	})
"""
urlpatterns = [
	path('message/', consumers.SendMessageConsumer.as_asgi(),)
]
