from django.db import models
from django.urls import reverse

# Create your models here.
from intereses.models import State, Area, Modalidad, tipoTrabajo
from company.models import Empresa


class Vacante(models.Model):
	company = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)
	jobrole = models.CharField(max_length=120, null=True, blank=True)
	tipo_trabajo = models.ForeignKey(tipoTrabajo, on_delete=models.CASCADE)
	modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)
	descripcion = models.TextField(max_length=2500)
	requisitos = models.TextField(max_length=2500)
	video_vacante = models.URLField(max_length=250, null=True, blank=True)
	sueldo = models.CharField(max_length=100, null=True, blank=True)
	pregunta_1 = models.CharField(max_length=250, null=True, blank=True)
	pregunta_2 = models.CharField(max_length=250, null=True, blank=True)
	pregunta_3 = models.CharField(max_length=250, null=True, blank=True)
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	city = models.CharField(max_length=100)

	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)



	class Meta:
		db_table = 'vacantes'
		ordering = ["-updated_at"]

	def get_absolute_url(self):
		return reverse('vacantes', args=[str(self.id)])


	def __str__(self):
		return str(self.company)
		