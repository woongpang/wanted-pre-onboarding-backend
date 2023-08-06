from django.urls import path
from users.views import SignUpView, LoginView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup_view"),
    path("login/", LoginView.as_view(), name="login_view"),
]