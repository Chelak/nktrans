from django.shortcuts import render,get_object_or_404
from django.utils import timezone

from .models import Article
# Create your views here.

def article(request,pk):
    single_article = get_object_or_404(Article, pk = pk)
    return render(request,'single_article.html',{'article': single_article})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

