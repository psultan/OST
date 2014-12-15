from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

import requests
import os

from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')

	
def test(request):
	return render_to_response('test.html')