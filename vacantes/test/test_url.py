from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import CreateVacanteView, SearchView

class TestUrls(SimpleTestCase):

	def test_members_list_url_is_resolved(self):
		url = reverse('vacantes-list')
		print(reslve(url))
		self.assertEquals(resolve(url).func, CreateVacanteView)

	def test_profile_create_url_is_resolved(self):
		url = reverse('vacante')
		print(reslve(url))
		self.assertEquals(resolve(url).func, SearchView)
