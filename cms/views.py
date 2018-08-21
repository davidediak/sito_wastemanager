from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from articles.models import Article
from django.urls import reverse_lazy
from .forms import RejectArticleForm


# Create your views here.
@staff_member_required
def pendingArticles(request):
    article_list_ord = Article.objects.order_by('-pub_date')
    latest_pending_articles = []
    for a in article_list_ord:
        if a.isPending():
            latest_pending_articles.append(a)
    context = {'latest_pending_articles': latest_pending_articles}
    return render(request, 'cms/cmsHome.html', context)


def detail(request, a_id):
    article =  get_object_or_404(Article, pk=a_id)
    context = {'article': article}
    return render(request, "cms/detailAdmin.html", context)



def approve(request, a_id):
    if request.user.is_superuser:
        article = get_object_or_404(Article, pk=a_id)
        article.status="APPROVED"
        article.save()
        return HttpResponseRedirect(
            reverse_lazy('cms:cmsHome'))
    else :
        return HttpResponse('You are not an Admin')



def reject(request, a_id):
    if request.user.is_superuser:
        if request.method == 'GET':
            article = get_object_or_404(Article, pk=a_id)
            form = RejectArticleForm(instance=article)
            return render(request, 'cms/articleForm.html', {'form':form})
        else:
            article = get_object_or_404(Article, pk=a_id)
            article.status = "REJECTED"
            article.save()
            f = RejectArticleForm(request.POST, instance=article)
            f.save()
            return HttpResponse('Article modified')
    else :
        return HttpResponse('You are not an Admin')
