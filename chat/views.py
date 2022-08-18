from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated

from chat.serializers import SendMessageSerializer, GetAllMsgSerializer
from chat.models import Message

from chat.connection import WebSocket
from channels.generic.websocket import WebsocketConsumer 
import websockets
import json

class SendMessageView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		msg = Message.objects.all()
		serializer = GetAllMsgSerializer(msg, many=True)
		return Response({'status': 200, 
			'message': 'estos son los mensajes que te han enviado', 
			'data': serializer.data})

	def post(self, request):
		data = request.data
		serializer = SendMessageSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response({'status': 201, 'message': 'tu mensaje ha sido enviado con exito'})
		return Response({'status': 400, 'message': 'algo no esta bien con tu informacion.'})

class GetMessagesView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request, message_id):
		msg = get_object_or_404(Message, pk=message_id)
		serializer = GetAllMsgSerializer(msg)
		return Response({'status': 200, 
			'message': 'Mensaje', 
			'data': serializer.data})

async def websocket_view(socket: WebSocket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        await socket.send_text(message)








