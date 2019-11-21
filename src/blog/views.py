from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,DeleteView
)

from .forms import ArticleModelForm 
from .models import Article

# Create your models here.
class ArticleListView(ListView):
    # overwrite template
    # template asli -> 'blog/namamodel_metod'
    # template_name = 'articles/<name>.html'

    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()

    # harusnya <:pk> di url tqapi diganti ke <:id>
    # kalo pake pk tidak usah pake metod get object
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # override get abosolute url kalo sudah berhasil
    success_url = '/'

    # cara validasi
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # override get abosolute url kalo sudah berhasil
    def get_success_url(self):
        return '/'

class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)
    # cara validasi
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    queryset = Article.objects.all()

    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)

    def get_success_url(self):
        return reverse('articles:article-list')