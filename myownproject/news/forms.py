from django import forms
from django.forms import ModelForm
import datetime


from models import *


class AddNewsForm(ModelForm):
	class Meta():
		model = News
		exclude = ('author','tags')
		
class AddTagsForm(forms.Form):
	tags = forms.CharField(max_length=100)