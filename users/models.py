from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import validate_email
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    password = models.CharField(max_length=128)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
