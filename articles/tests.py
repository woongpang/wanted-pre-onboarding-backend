from users.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from articles.models import Article
from rest_framework_simplejwt.tokens import RefreshToken


class ArticleTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser", password="1!2@3#4$asdf")
        self.token = RefreshToken.for_user(self.user)

        self.client = APIClient()
        self.client.force_authenticate(user=self.user, token=self.token)

        self.article = Article.objects.create(
            author=self.user, title="Test Article", content="Test Content"
        )

    def test_create_article(self):
        response = self.client.post(
            "/articles/create/",
            data={"title": "Test Article", "content": "Test Content"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Test Article")
        self.assertEqual(response.data["content"], "Test Content")
        self.assertEqual(response.data["author"], self.user.id)

    def test_list_articles(self):
        response = self.client.get("/articles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_detail_article(self):
        response = self.client.get(f"/articles/{self.article.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Article")
        self.assertEqual(response.data["content"], "Test Content")

    def test_update_article(self):
        response = self.client.put(
            f"/articles/{self.article.id}/edit/",
            data={"title": "Updated Article", "content": "Updated Content"},
            format="json",  # 여기에 JSON 포맷을 지정
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Article")
        self.assertEqual(response.data["content"], "Updated Content")

    def test_delete_article(self):
        response = self.client.delete(f"/articles/{self.article.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(Article.DoesNotExist, Article.objects.get, id=self.article.id)
