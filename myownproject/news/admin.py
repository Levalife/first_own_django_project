from django.contrib import admin
from models import News, Category, Tag

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'category' ,'author', 'news_body', 'pub_date')
	ordering = ('pub_date',)
	filter_horizontal = ('tags',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)