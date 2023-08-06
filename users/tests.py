from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from users.models import User


class SignUpViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.sign_up_url = reverse("signup_view")

    def test_sign_up_with_valid_data(self):
        data = {
            "email": "test@example.com",
            "password": "1!2@3#4$asdf",
            "password2": "1!2@3#4$asdf",
        }
        response = self.client.post(self.sign_up_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

    def test_sign_up_with_mismatched_password(self):
        data = {
            "email": "test@example.com",
            "password": "1!2@3#4$asdf",
            "password2": "differentpassword",
        }
        response = self.client.post(self.sign_up_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sign_up_with_invalid_email(self):
        data = {
            "email": "testexample.com",
            "password": "1!2@3#4$asdf",
        }
        response = self.client.post(self.sign_up_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sign_up_with_short_password(self):
        data = {
            "email": "test@example.com",
            "password": "short",
        }
        response = self.client.post(self.sign_up_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sign_up_with_existing_email(self):
        existing_user = User.objects.create(
            email="test@example.com", password="1!2@3#4$asdf"
        )
        data = {
            "email": "test@example.com",
            "password": "1!2@3#4$asdf",
        }
        response = self.client.post(self.sign_up_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
