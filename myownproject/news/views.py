from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from models import News, Category, Tag
from forms import AddNewsForm, AddTagsForm

def news_page(request, news_id):
	news = News.objects.get(pk=news_id)
	tags = news.tags.all()
	return render(request, 'news/newspage.html', {'news': news, 'tags': tags})

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

#def edit_news(request, news_is):
#	news = news.objects.get(pk=news_id)
#	form = EditNewsForm(request.POST, instance = news)
#	form.save()