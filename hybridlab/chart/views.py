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
               'source': Current.objects.filter(id_simulation=simulation)},
              'terms': [
                'current',
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
                    'current']
                  }}],
            chart_options =
              {'title': {
              	'text': 'Grafico de Corrente x Tempo'},
                'colors': ['#3AA6D0'],
                'chart': {'backgroundColor': '#DAEEF2'},
               'xAxis': {
                    'title': {
                       'text': 'Tempo (s)'}},
                'yAxis': {
                    'title': {
                       'text': 'Corrente (A)'}}})

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
                'text': 'Grafico de Consumo(l/s) x Tempo(s)'},
                'colors': ['#3AA6D0'],
                'chart': {'backgroundColor': '#DAEEF2'},
               'xAxis': {
                    'title': {
                       'text': 'Tempo (s)'}},
                'yAxis': {
                    'title': {
                       'text': 'Consumo (l/s)'}}})

        return render_to_response('resultados.html',{'resultados' : [cht, chtT], 'simulation': simulation})
