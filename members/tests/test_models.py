from django.test import TestCase
from members.models import Persona

class TestModel(TestCase):

	def setUp(self):
		self.person32 = Persona.objects.create(
			first_name='carolina',
			last_name='mendoza',
			last_name_m='medina',
			birth_date='1989-12-13',
			age=33,
			genero=1,
			civil_status=1,
			state=4,
			residence='utopia',
		)

