from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registration(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			messages.info(request, "You've successfully registered")
			return HttpResponseRedirect('/')
	else:
		form = UserCreationForm
	return render(request, 'accounts/registration.html', {'form': form})