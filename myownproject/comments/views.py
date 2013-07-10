from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, render_to_response

from models import Comment
from forms import AddCommentForm
from news.models import News

''''
def add_comment(request, news_id):
	news = News.objects.get(pk=news_id)
	print 111
	if request.method == 'POST':
		print 2222
		form = AddCommentForm(request.POST)
		if form.is_valid:
			comment = form.save(commit=False)
			comment.author = request.user
			comment.news = news
			comment.save()
		print 333
	form = AddCommentForm()
	print 567978987
	return render_to_response(request, 'news/news_page.html', {'form': form})

''''