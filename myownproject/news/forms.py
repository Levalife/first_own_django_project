from django.forms import ModelForm
import datetime


from models import *


class AddNewsForm(ModelForm):
	class Meta():
		model = News
		exclude = ('author',)
		