from django.contrib.auth import authenticate
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from users.models import User
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or "@" not in email or password is None or len(password) < 8:
            return Response(
                {
                    "error": "이메일과 비밀번호는 비워둘 수 없으며, 이메일에는 '@'가 포함되어야 하고, 비밀번호는 8자 이상이어야 합니다."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "이미 존재하는 이메일입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        password = make_password(password)
        user = User.objects.create(email=email, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
