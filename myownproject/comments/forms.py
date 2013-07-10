from django.forms import ModelForm
from django import forms
from models import Comment

class AddCommentForm(ModelForm):
	comment_body = forms.CharField(widget=forms.Textarea)

	class Meta():
		model = Comment
		exclude = ('author', 'news','pub_date',)