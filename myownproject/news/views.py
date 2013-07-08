from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from models import News, Category
from forms import AddNewsForm

def news_page(request, news_id):
	news = News.objects.get(pk=news_id)
	tags = news.tags.all()
	return render(request, 'news/newspage.html', {'news': news, 'tags': tags})

@login_required
def add_news(request):
	cats = Category.objects.all()
	if request.method == "POST":
		form = AddNewsForm(request.POST)
		
		
		##news = form (request.POST['title'], request.POST['category'], request.user, request.POST['news_body'], request.POST['pub_date'], request.POST['tags'])
		if form.is_valid():
			news = form.save(commit=False)
			news.author = request.user
			news.save()
			messages.info(request, "You've successfully added news")
			return HttpResponseRedirect('/')
		else:
			print form['category']
			messages.info(request, "Fill all fields")
	else:
		form = AddNewsForm()
	return render(request, 'news/add_news.html', {'form': form})

#def edit_news(request, news_is):
#	news = news.objects.get(pk=news_id)
#	form = EditNewsForm(request.POST, instance = news)
#	form.save()