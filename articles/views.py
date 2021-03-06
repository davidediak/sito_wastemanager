from django.shortcuts import render, get_object_or_404
from articles.models import Article
from .forms import WriteArticleForm
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from crm.models import ArticleHit, SessionBind

# Create your views here.
def index(request):
    article_list_ord = Article.objects.filter(status="APPROVED").order_by('-pub_date')
    context = {'latest_pending_articles': article_list_ord}
    return render(request, 'articles/index.html', context)

@login_required
def write(request):
    if request.method=='GET':
        form=WriteArticleForm()
        return render(request, 'articles/writeForm.html', {'form':form})
    else:
        # Create a form instance from POST data.
        f = WriteArticleForm(request.POST)
        # Save a new Author object from the form's data.
        new_article = f.save(commit=False)
        new_article.pub_date = timezone.now()
        new_article.author = request.user
        if request.user.is_superuser:
            new_article.status = 'APPROVED'
        new_article.save()
        return HttpResponse('New article completed !')


def detail(request, a_id):
    article =  get_object_or_404(Article, pk=a_id)

    #questo serve per creare una session key anche per gli anon users, di default django non lo fa
    if not request.session or not request.session.session_key:
        request.session.save()
    #conto le visualizzazioni all'articolo, per ogni session key -> articolo.hits += 1
    if not ArticleHit.objects.filter( article=article, custom_session_key=SessionBind.objects.get(django_session_key=request.session.session_key).id ):
        hit = ArticleHit(article=article, ip=request.META['REMOTE_ADDR'], created=timezone.now(), custom_session_key=SessionBind.objects.get( django_session_key=request.session.session_key).id )
        hit.save()

    context = {'article': article}
    if article.isPending() & request.user.is_superuser:
        return render(request, "articles/detailAdmin.html", context)
    else:
        return render(request, "articles/detail.html", context)


'''
def modify(request, a_id):
    if request.user.is_superuser:
        if request.method=='GET':
            a = Article.objects.get(pk=a_id)
            form = ArticleForm(instance=a)
            return render(request, 'articles/writeForm.html', {'form':form})
        else:
            a = Article.objects.get(pk=a_id)
            f = ArticleForm(request.POST, instance=a)
            # Save a new Author object from the form's data.
            f.save()
            return HttpResponse('Article modified')
    else :
        return HttpResponse('You are not an Admin')
'''