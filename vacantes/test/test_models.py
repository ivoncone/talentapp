from django.test import TestCase
from members.models import Persona

class TestModel(TestCase):

	def setUp(self):
		self.vacante30 = Persona.objects.create(
			company = self.client,
			area=1,
			jobrole=1,
			tipo_trabajo=1,
			modalidad=1,
			descripcion='desarrollador de proyectos de it',
			requisitos='catalogo de proyectos anteriores',
			sueldo='30000',
			state=1,
			city='utopia'
			
		)