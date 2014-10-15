from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))


def history(request):
	return render_to_response('historico.html', context_instance=RequestContext(request))