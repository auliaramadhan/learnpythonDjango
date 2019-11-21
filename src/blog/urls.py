from django.urls import path
from .views import (
    ArticleListView
    ,ArticleDetailView
    ,ArticleCreateView
    ,ArticleUpdateView
    ,ArticleDeleteView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView, name='article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView, name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView, name='article-delete'),
]