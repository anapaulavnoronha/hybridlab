from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.generic import ListView
from chart.models import *
from chartit import DataPool, Chart

# Create your views here.

class ListSimulationtView(ListView):
	model = Simulation
	template_name = 'historico.html'

def resultados(request, SimuId):
	simulation = Simulation.objects.get(id=SimuId)

	simulationdata = \
        DataPool(
           series=
            [{'options': {
               'source': Tension.objects.filter(id_simulation=simulation)},
              'terms': [
                'tension',
                'time']},
        	{'options': {
            	'source': Fuel.objects.filter(id_simulation=simulation)},
          		'terms': [
            	{'time_fuel': 'time'}, 
            	'fuel']}
            ])
        cht = Chart(
            datasource = simulationdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'tension': [
                    'time'],
                    'fuel':[
                    'time_fuel']
                  }}],
            chart_options =
              {'title': {
              	'text': 'Dados da Simulacao Realizada'},
               'xAxis': {
                    'title': {
                       'text': 'Time'}}})
        return render_to_response('resultados.html',{'resultados': cht})