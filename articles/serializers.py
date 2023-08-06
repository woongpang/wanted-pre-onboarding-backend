from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    is_author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ("id", "author", "title", "content", "created_at", "is_author")
        read_only_fields = ("author",)

    def get_is_author(self, article):
        request = self.context["request"]
        return article.author == request.user
