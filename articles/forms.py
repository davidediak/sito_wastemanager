from django.forms import ModelForm
from articles.models import Article
from django import forms


class WriteArticleForm(ModelForm):

    class Meta:
        model=Article
        fields= ['title', 'content']


