from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_index(request):
    news = Article.objects.order_by('date')
    return render(request, 'news/news_index.html', {'news': news})

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article' # его мы можем исп в нашем html

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/' # переадресация после удаления
    template_name = 'news/news-delete.html'

def create(request):
    err = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST) # получаем данные от пользователья
        if form.is_valid(): # Этот метод наследуется от класса ModelForm
            form.save()
            return redirect('news_index') # переадресани на страницу новостей
        else:
            err = 'Ошибка заполнения формы'

    form = ArticleForm()

    data = {
        'form': form,
        'err': err,
    }
    return render(request, 'news/create.html', data)