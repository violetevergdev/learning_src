from django.shortcuts import render
from .models import Article

def news_index(request):
    news = Article.objects.order_by('date')
    return render(request, 'news/news_index.html', {'news': news})
