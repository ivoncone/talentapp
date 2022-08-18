from django.test import TestCase, Client
from django.urls import reverse
from members.models import Persona
import json



class TestViews(TestCase):
	def setUp(self):
		self.client = Client()
		self.list_url = reverse('talent')
		self.add_person = reverse('profile', args=['carolina'])
		Persona.objects.create(
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
		
	def test_personas_list_GET(self):
		client = Client()
		response = client.get(reverse('talent'))
		self.assertEquals(response.status_code, 200)

	def test_persona_POST_add_new_person(self):
		Persona.objects.create(
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
		response = self.client.post(self.add_person, {
				'first_name':'carolina',
				'last_name':'mendoza',
				'last_name_m':'medina',
				'birth_date':'1989-12-13',
				'age':33,
				'genero':1,
				'civil_status':1,
				'state':4,
				'residence':'utopia',
			})
		self.assertEquals(response.status_code, 302)
		self.assertEquals(self.carolina.persona.first().first_name, 'carolina')


	def test_persona_DELETE(self):
		carolina = Persona.objects.create(
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
		Persona.objects.create(
			persona=self.carolina,
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

		response = self.client.delete(self.add_person, json.dumps({
			'id':20
		}))

		self.assertEquals(response.status_code, 204)
		self.assertEquals(self.carolina.persona.count(), 0)

	def test_persona_create_POST(self):
		url = reverse('profile')
		response = self.client.post(url, {
				'first_name':'carolina',
				'last_name':'mendoza',
				'last_name_m':'medina',
				'birth_date':'1989-12-13',
				'age':33,
				'genero':1,
				'civil_status':1,
				'state':4,
				'residence':'utopia',

			})

		carolina = Persona.objects.get(id=20)
		self.assertEquals(carolina.first_name, 'carolina')
		persona = Persona.objects.get(id=20)
		self.assertEquals(first_person.persona, carolina)
		self.assertEquals(first_person.first_name, 'carolina') 

