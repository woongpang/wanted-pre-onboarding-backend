from django.urls import path
from users.views import SignUpView, CustomTokenObtainPairView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup_view"),
    path(
        "login/",
        CustomTokenObtainPairView.as_view(),
        name="custom_token_obtain_pair",
    ),
]
