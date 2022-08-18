from django.db import models
from users.models import User
from channels.layers import get_channel_layer 
from asgiref.sync import async_to_sync
import json

class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Notification = models.TextField(max_length=100)
	is_seen = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		channel_layer = get_channel_layer()
		notification_objs = Notification.objects.all(is_seen=False).count()
		data = {'count': notification_objs, 'current_notification': self.notification}
		async_to_sync(channel_layer.group_send)(
			'test_consumer_group', {
				'type': 'send_notification',
				'value': json.dumps(data)
			}
			)
		super(Notification, self).save(*args, **kwargs)

	class Meta:
		db_table = 'notificaciones'

	def __str__(self):
		return str(self.id)

class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'mensajes'

	def __str__(self):
		return str(self.id)
















