from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

import requests
import os

from .models import Greeting, Test
from forms import TestForm

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')

	
def all(request):
	return render_to_response('all.html', {'tests': Test.objects.all()})
	
def create(request):
	if request.POST:
		#save form
		form = TestForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/hello/all')
	else:
		#show form
		form = TestForm()
		args={}
		args['form'] = form
		return render_to_response("create_test.html", args, context_instance=RequestContext(request))