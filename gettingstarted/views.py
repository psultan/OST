from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')
def current_user(request):
	user = request.user
	if user.is_authenticated():
		s = ""
		s+="username:"+str(user.username)
		s+="<br>first_name:"+str(user.first_name)
		s+="<br>last_name:"+str(user.last_name)
		s+="<br>email:"+str(user.email)
		s+="<br>password:"+str(user.password)
		s+="<br>is_staff:"+str(user.is_staff)
		s+="<br>is_active:"+str(user.is_active)
		s+="<br>is_superuser:"+str(user.is_superuser)
		s+="<br>last_login:"+str(user.last_login)
		s+="<br>date_joined:"+str(user.date_joined)
	else:
		s="No User"
	return HttpResponse('<pre>' + s + '</pre>')
def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/accounts/register_success")
		else:
			return invalid_login(request)
	else:
		form = UserCreationForm()
		return render(request, "register.html", {'form': form}, context_instance=RequestContext(request))
def register_success(request):
	return render_to_response('register_success.html')
def login(request):
	return render_to_response('login.html', context_instance=RequestContext(request))
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
def loggedin(request):
	return render_to_response('loggedin.html', {'full_name':request.user.username})
def invalid_login(request):
	return render_to_response('invalid_login.html')
