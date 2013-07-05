from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login as auth_login


from accounts.forms import LoginForm

def registration(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			print form.cleaned_data['password']
			messages.info(request, "You've successfully registered")
			return HttpResponseRedirect('/')
	else:
		form = UserCreationForm
	return render(request, 'accounts/registration.html', {'form': form})

'''
def login(request):
	print 0000000000000000000
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			userData = form.cleaned_data
			user = authenticate(username=userData['username'], password=userData['password'])
			print 55555555555555555555
			user1 = User.objects.get(username='Tanya')
			print userData['password']
			print user1.password
			print user
			auth_login(request, user)
			print 6666666666666666666
			messages.info(request, "You're successfully logged in")
			return HttpResponseRedirect('/')
		else:
			messages.info(request, 'Invalid username or password')
			return HttpResponseRedirect('/accounts/login')
	else:
		print 22222222222222222
		form = LoginForm() 
	return render(request, 'accounts/login.html', {'form': form})
'''	
	