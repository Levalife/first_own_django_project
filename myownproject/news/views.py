from django.shortcuts import render
from models import News

def news_page(request, news_id):
	news = News.objects.get(pk=news_id)
	tags = news.tags.all()
	return render(request, 'news/newspage.html', {'news': news, 'tags': tags})

def add_news(request):
	if request.method == "POST":
		form = AddNewsForm(request.POST)
