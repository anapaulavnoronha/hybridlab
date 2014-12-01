from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
# Create your views here.

# def contact(request):
# 	return render_to_response('contato.html', context_instance=RequestContext(request))
# 
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Insira um Assunto!')
        if not request.POST.get('message', ''):
            errors.append('Insira uma Mensagem!')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Insira um E-mail valido!')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                None,
                ['hybridlab.fga@gmail.com'], 
                fail_silently=False
                #email address where message is sent.
            )
            return HttpResponseRedirect('/thanks/')
    return render(request, 'contact.html',
        {'errors': errors})

def thanks(request):
    return render_to_response('thanks.html')