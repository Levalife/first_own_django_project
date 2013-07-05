from django import forms
import datetime

class AddNewsForm(forms.Form):
	title
	category
	news_body
	pub_date = forms.DateTimeField()
	tags