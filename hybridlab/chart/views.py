from django.shortcuts import render_to_response, render
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

	simulationdataTension = \
        DataPool(
           series=
            [{'options': {
               'source': Tension.objects.filter(id_simulation=simulation)},
              'terms': [
                'tension',
                'time']}
            ])
        cht = Chart(
            datasource = simulationdataTension,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'time': [
                    'tension']
                  }}],
            chart_options =
              {'title': {
              	'text': 'Dados da Tensao da Simulacao Realizada'},
                'colors': ['#3AA6D0'],
                'chart': {'backgroundColor': '#FFFFFF'},
               'xAxis': {
                    'title': {
                       'text': 'Time'}}})

        simulationdataFuel = \
        DataPool(
           series=
            [{'options': {
              'source': Fuel.objects.filter(id_simulation=simulation)},
              'terms': [
              'time', 
              'fuel']}
            ])
        chtT = Chart(
            datasource = simulationdataFuel,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'time': [
                    'fuel']
                  }}],
            chart_options =
              {'title': {
                'text': 'Dados do Consumo da Simulacao Realizada'},
                'colors': ['#3AA6D0'],
                'chart': {'backgroundColor': '#FFFFFF'},
               'xAxis': {
                    'title': {
                       'text': 'Time'}}})

        return render_to_response('resultados.html',{'resultados' : [cht, chtT], 'simulation': simulation})
