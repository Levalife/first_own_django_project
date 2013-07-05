from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput)

