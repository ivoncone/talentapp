from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
from users.models import User

from django.contrib.auth.models import PermissionsMixin


# Crear modelo de empresa
class Empresa(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	empresa = models.CharField(max_length=250)
	descrip = models.CharField(max_length=300, null=True) 
	web = models.URLField(max_length=250, unique=True)
	rfc = models.CharField(max_length=20, unique=True)
	logo = CloudinaryField('image', null=True, default='https://res.cloudinary.com/posdatamexicogallery/image/upload/v1656036804/avatares/default_riyo2u.jpg')
	is_approved = models.BooleanField(default=False)
	is_declined = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'empresas'
		ordering = ["-updated_at"]


	def __str__(self):
		return str(self.user)



