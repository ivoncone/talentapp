from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import UserView, ProfileCreate, ApplicantsView

class TestUrls(SimpleTestCase):

	def test_members_list_url_is_resolved(self):
		url = reverse('talent')
		print(reslve(url))
		self.assertEquals(resolve(url).func, ApplicantsView)

	def test_profile_create_url_is_resolved(self):
		url = reverse('profile')
		print(reslve(url))
		self.assertEquals(resolve(url).func, ProfileCreate)

