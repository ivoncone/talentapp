import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer 

class SendMessageConsumer(WebsocketConsumer):

	def connect(self):
		self.room_name = "message"
		self.room_group_name = "consumer_group"
		async_to_sync(self.channel_layer.group_send)(
			self.room_name, self.room_group_name
		)

		self.accept()
		self.send(text_data=json.dumps({'status': 200, 'message': 'welcome to get talent app'}))

	# {'user_id': 1, 'message': hi}
	def receive(self, text_data):
		self.send(text_data=json.dumps(text_data)) 

	def disconnect(self, *args, **kwargs):
		print('disconnect')

	def send_notification(self, event):
		print('send notificaction')
		data = json.loads(event.get('value'))
		self.send(text_data=({'payload': data}))
		print('send notificaction')

		 










