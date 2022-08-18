from django.urls import path
from chat import views
from chat.views import SendMessageView, GetMessagesView, websocket_view

websocket = path

urlpatterns = [
	path("message/send/", views.SendMessageView.as_view()),
	path("message/<int:message_id>/", views.GetMessagesView.as_view())
]