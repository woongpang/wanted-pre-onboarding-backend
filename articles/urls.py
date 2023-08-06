from django.urls import path
from articles.views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]
