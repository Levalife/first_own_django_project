from django.db import models
from news.models import News
from django.contrib.auth.models import User
import datetime

class Comment(models.Model):
	author = models.ForeignKey(User)
	comment_body = models.CharField(max_length=500)
	news = models.ForeignKey(News)	
	pub_date = models.DateTimeField(default = datetime.datetime.now())