from django.test import TestCase, Client
from django.urls import reverse
from members.models import Empresa
import json



class TestViews(TestCase):
	def setUp(self):
		self.client = Client()
		self.list_url = reverse('waiting-list')
		self.add_company = reverse('company', args=['lucky natural store'])
		Empresa.objects.create(
			empresa='lucky naturals store',
			descrip='tienda de productos naturales',
			web='https://www.luckymedicine.com',
			rfc='LUKY9506231DT',
		)
		
	def test_companies_list_GET(self):
		client = Client()
		response = client.get(reverse('waiting-list'))
		self.assertEquals(response.status_code, 200)

	def test_company_POST_add_new_person(self):
		Empresa.objects.create(
			empresa='lucky naturals store',
			descrip='tienda de productos naturales',
			web='https://www.luckymedicine.com',
			rfc='LUKY9506231DT'
		)

		response = self.client.post(self.add_company, {
				'empresa':'lucky naturals store',
				'descrip':'tienda de productos naturales',
				'web':'https://www.luckymedicine.com',
				'rfc':'LUCKY9506231DT'
			})
		self.assertEquals(response.status_code, 302)
		self.assertEquals(self.empresa6.companies.first().empresa, 'lucky naturals store')

	def test_company_DELETE(self):
		Empresa.objects.create(
			empresa=self.empresa6,
			empresa='lucky naturals store',
			descrip='tienda de productos naturales',
			web='https://www.luckymedicine.com',
			rfc='LUKY9506231DT'	
		)

		response = self.client.delete(self.add_company, json.dumps({
			'id':30
			}))

		self.assertEquals(response.status_code, 204)
		self.assertEquals(self.empresa6.companies.count(), 0)