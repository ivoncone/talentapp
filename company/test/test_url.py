from django.test import SimpleTestCase
from django.urls import reverse, resolve
from company.views import CompanyView, CompanyWaitingListView

class TestUrls(SimpleTestCase):

	def test_members_list_url_is_resolved(self):
		url = reverse('waiting-list')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, CompanyWaitingListView)

	def test_profile_create_url_is_resolved(self):
		url = reverse('company')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, CompanyView)