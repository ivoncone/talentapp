from django.db import models

# Create your models here.
from members.models import Persona
from vacantes.models import Vacante

class Application(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
	vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
	video = models.URLField(max_length=250, blank=True, null=True)
	is_active = models.BooleanField(default=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'applications'
		ordering = ["-updated_at"]


	def __str__(self):
		return str(self.vacante)