from django.db import models

# Create your models here.


from django.db import models

# Create your models here.
class State(models.Model):
	state = models.CharField(max_length=100, unique=True)

	class Meta:
		db_table = 'estados'

	def __str__(self):
		return str(self.state)
		
class jobRole(models.Model):
	jobrole = models.CharField(max_length=100)

	class Meta:
		db_table = 'jobs'

	def __str__(self):
		return str(self.jobrole)

class Area(models.Model):
	area = models.CharField(max_length=100, unique=True)

	class Meta:
		db_table = 'intereses'

	def __str__(self):
		return str(self.area)

class tipoTrabajo(models.Model):
	tipo_trabajo = models.CharField(max_length=100, unique=True)

	class Meta:
		db_table = 'jobshours'

	def  __str__(self):
		return str(self.tipo_trabajo)

class Modalidad(models.Model):
	modalidad = models.CharField(max_length=100, unique=True)

	class Meta:
		db_table = 'modalities'


	def __str__(self):
		return str(self.modalidad)