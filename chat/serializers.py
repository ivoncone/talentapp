from chat.models import Message 

from rest_framework import serializers

class SendMessageSerializer(serializers.ModelSerializer):

	class Meta:
		model = Message
		fields = ['user', 'content']

class GetAllMsgSerializer(serializers.ModelSerializer):

	class Meta:
		model = Message
		fields = ['user', 'content', 'created_at']