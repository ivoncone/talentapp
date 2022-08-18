from django.test import TestCase

class TestModels(TestCase):

	def setUp(self):
		self.empresa6 = Empresa.objects.create(
			empresa='lucky naturals store',
			descrip='tienda de productos naturales',
			web='https://www.luckymedicine.com',
			rfc='LUKY9506231DT',
		)

	