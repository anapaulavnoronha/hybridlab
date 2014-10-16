from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from chart.models import Simulation

# Create your views here.

class ListSimulationtView(ListView):
	model = Simulation
	template_name = 'historico.html'
