from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from chart.models import *
# Create your tests here.

class ListSimulationViewTest(TestCase):
	def test_response_simulation(self):
		client = Client()
		response = client.get(reverse('history'))
		self.failUnlessEqual(response.status_code, 200)


	def test_template_simulation(self):
		client = Client()
		response = client.get(reverse('history'))
		self.assertTemplateUsed(response, 'historico.html', 'base.html')

class ResultadosViewTest(TestCase):
	def test_response_resultados(self):
		client = Client()
		Simulation.objects.create();
		s = Simulation.objects.get(id=1)
		response = client.get(reverse('resultados', args = [s.id]))
		self.failUnlessEqual(response.status_code, 200)

	def test_template_resultados(self):
		client = Client()
		Simulation.objects.create();
		s = Simulation.objects.get(id=1)
		response = client.get(reverse('resultados', args = [s.id]))
		self.assertTemplateUsed(response.status_code, 'resultados.html', 'base.html')