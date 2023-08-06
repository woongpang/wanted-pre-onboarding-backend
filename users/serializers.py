from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ("email", "password")

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError('Email must contain "@" symbol.')
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            password=make_password(validated_data["password"]),  # 비밀번호 암호화
        )
        user.save()
        return user
