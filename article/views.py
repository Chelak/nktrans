from django.shortcuts import render
from django.utils import timezone

from .models import Article
# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

