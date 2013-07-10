from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from models import News, Category, Tag
from forms import AddNewsForm, AddTagsForm, EditNewsForm
from comments.models import Comment
from comments.forms import AddCommentForm
#from comments.views import add_comment


def news_page(request, news_id):
	news = News.objects.get(pk=news_id)
	tags = news.tags.all()
	category = news.category
	comments = news.comment_set.all()
	if request.method == 'POST':
		form = AddCommentForm(request.POST)
		if form.is_valid:
			comment = form.save(commit=False)
			comment.author = request.user
			comment.news = news
			comment.save()
	form = AddCommentForm()
	#form = add_comment(request, news.id)
	return render(request, 'news/news_page.html', {'form': form, 'news': news, 'tags': tags, 'category': category, 'user': request.user, 'comments': comments})
	

@login_required
def add_news(request):
	if request.method == "POST":
		form = AddNewsForm(request.POST)
		tform = AddTagsForm(request.POST or None)
		if form.is_valid():
			news = form.save(commit=False)
			tags = request.POST['tags'].split()
			news.author = request.user
			news.save()
			for tag in tags:
				new_tag = Tag(tag=tag)
				if Tag.objects.filter(tag=new_tag).exists():
					new_tag= Tag.objects.get(tag=tag)
				else:
					new_tag.save()
				news.tags.add(new_tag)
			messages.info(request, "You've successfully added news")
			return HttpResponseRedirect('/')
		else:
			messages.info(request, "Fill all fields")
	else:
		form = AddNewsForm()
	return render(request, 'news/add_news.html', {'form': form})

def edit_news(request, news_id):
	news = News.objects.get(pk=news_id)
	if request.method == "POST":
		form = EditNewsForm(request.POST, instance = news)
		if form.is_valid():
			news = form.save()
			messages.info(request, 'Your changes successfully saved')
			return HttpResponseRedirect('/news/%s/' %news.id)
		else:
			messages.info(request, "Fill all fields")
	else:
		form = EditNewsForm(instance = news)
	return render(request, 'news/edit_news.html', {'form': form})

def news_by_tag(request, tag_id):
	tag = Tag.objects.get(pk=tag_id)
	news = tag.news_set.all()
	return render(request, 'news/news_by_tag.html', {'tag': tag, 'news': news})

def news_by_cat(request, category_id):
	category = Category.objects.get(pk=category_id)
	news = category.news_set.all()
	return render(request, 'news/news_by_cat.html', {'category': category, 'news': news})
'''
def add_comment(request, news_id):
	news = News.objects.get(pk=news_id)
	if requesr.method == 'POST':
		form = AddCommentForm(request.POST)
		if form.is_valid:
			comment = form.save()
			comment.author = request.User
			comment.news = news
			comment.save()
			return HttpResponseRedirect(request, '/news/%s/' %news.id)
		else:
			message.info(request, 'Fill form correct')
	else:
		form = AddCommentForm()
	return HttpResponseRedirect(request, '/news/%s/' %news.id)
'''