from django.contrib.auth import authenticate
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import User
from django.contrib.auth.hashers import make_password


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)

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


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

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

        user = authenticate(username=email, password=password)
        if user is None:
            return Response(
                {"error": "유효하지 않은 이메일 또는 비밀번호입니다."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)

        return Response({"token": token}, status=status.HTTP_200_OK)
