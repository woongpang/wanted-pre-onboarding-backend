from django.urls import path
from articles.views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("articles/<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path(
        "articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"
    ),
]
