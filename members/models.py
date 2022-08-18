from django.db import models
from django.urls import reverse
from users.models import User
from intereses.models import State, Area, Modalidad, tipoTrabajo
from cloudinary.models import CloudinaryField


from django.contrib.auth.models import PermissionsMixin


class Gender(models.Model):
	genero = models.CharField(max_length=100, unique=True, null=True)

	class Meta:
		db_table = 'genders'

	def __str__(self):

		return str(self.genero)

class CivilStatus(models.Model):
	civil_status = models.CharField(max_length=100, unique=True, null=True)

	class Meta:
		db_table = 'civilstatus'

	def __str__(self):

		return self.civil_status

#modelo para la lista precargada H6
class NivelAcademico(models.Model):
    nivel_academico = models.CharField(max_length=100)
    class Meta:
        db_table = 'nivel' #hace referencia a la tabla en la bd
    def __str__(self):
        return self.nivel_academico

#finalizado, trunco etc
class Status(models.Model):
    status = models.CharField(max_length=100)
    class Meta:
        db_table = 'status'
    def __str__(self):
        return self.status

#solicitante 
class DatosAcademicos(models.Model):
    nivel_academico = models.ForeignKey(NivelAcademico, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=250)
    institucion = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #se le asigna la fecha cuando se registra
    updated_at= models.DateTimeField(auto_now_add=True) #se puede actualizar a futuro, cada vez que haya un PUT


    class Meta:
        db_table = 'datos_academicos'
    
    def __str__(self):
        return str(self.nombre)



# Create modelo solicitante
class Persona(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	last_name_m = models.CharField(max_length=120, null=True, blank=True)
	genero = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
	birth_date = models.DateField()
	civil_status = models.ForeignKey(CivilStatus, on_delete=models.CASCADE, null=True)
	age = models.IntegerField()
	state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

	datosAcademicos = models.ManyToManyField(DatosAcademicos)

	residence = models.CharField(max_length=120)
	area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
	jobrole = models.CharField(max_length=120, blank=True, null=True)
	modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, null=True)
	tipo_trabajo = models.ForeignKey(tipoTrabajo, on_delete=models.CASCADE, null=True)
	image = CloudinaryField('image', default='https://res.cloudinary.com/posdatamexicogallery/image/upload/v1656036804/avatares/default_riyo2u.jpg')
	
	video = models.URLField(max_length=200, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'personas'
	
	def __str__(self):

		return str(self.first_name)

