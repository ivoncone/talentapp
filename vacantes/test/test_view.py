from django.test import TestCase, Client

from django.urls import reverse
from vacantes.models import Vacante
import json


class TestViews(TestCase):
	def setUp(self):
		self.client = Client()
		self.list_url = reverse('vacantes-list')
		self.add_vacante = reverse('vacante')
		Vacante.objects.create(
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
		
	def test_companies_list_GET(self):
		client = Client()
		response = client.get(reverse('vacantes-list'))
		self.assertEquals(response.status_code, 200)

	def test_company_POST_add_new_person(self):
		Vacante.objects.create(
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

		response = self.client.post(self.add_company, {
			'company':self.client,
			'area':1,
			'jobrole':1,
			'tipo_trabajo':1,
			'modalidad':1,
			'descripcion':'desarrollador de proyectos de it',
			'requisitos':'catalogo de proyectos anteriores',
			'sueldo':'30000',
			'state':1,
			'city':'utopia'
			})
		self.assertEquals(response.status_code, 302)
		self.assertEquals(self.vacante30.vacantes.first().descripcion, 'desarrollador de proyectos de it')

	def test_company_DELETE(self):
		Vacante.objects.create(
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

		response = self.client.delete(self.add_vacante, json.dumps({
			'id':30
			}))

		self.assertEquals(response.status_code, 204)
		self.assertEquals(self.vacante30.vacantes.count(), 0)