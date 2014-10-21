from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
# Create your tests here.


class ViewTestCase(TestCase):

	def test_response_home(self):
		client = Client()
		response = client.get(reverse('home'))

		self.failUnlessEqual(response.status_code, 200)

	def test_template_home(self):
		client = Client()
		response = client.get(reverse('home'))

		self.assertTemplateUsed(response, 'index.html', 'base.html')