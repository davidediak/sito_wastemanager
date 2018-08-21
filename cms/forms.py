from django.forms import ModelForm
from articles.models import Article
from django import forms


class RejectArticleForm(ModelForm):

    class Meta:
        model=Article
        fields= ['title', 'content']

    reject_motivation = forms.CharField(widget=forms.Textarea)