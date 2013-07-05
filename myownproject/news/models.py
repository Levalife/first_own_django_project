from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
	category = models.CharField(max_length=20)

	def __unicode__(self):
		return self.category

class Tag(models.Model):
	tag = models.CharField(max_length=30, blank=True)
	

	def __unicode__(self):
		return self.tag

class News(models.Model):
	title = models.CharField(max_length=80)
	category = models.ForeignKey(Category)
	author = models.ForeignKey(User)
	news_body = models.CharField(max_length=5000)
	pub_date = models.DateField(default = datetime.datetime.now())
	tags = models.ManyToManyField(Tag, blank=True)

	def __unicode__(self):
		return self.title

		