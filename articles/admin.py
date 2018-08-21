from django.contrib import admin
from .models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

 list_display = ('title', 'author', 'pub_date', 'status')
 list_filter = ['pub_date']
 search_fields = ['title']

admin.site.register(Article, ArticleAdmin)