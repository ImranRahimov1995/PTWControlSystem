from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    USERNAME_FIELD = "username"

    email = models.EmailField(
        unique=True, error_messages={
            'unique': "A user with that email already exists"
        }, db_index=True,
    )

    def __str__(self):
        return self.get_full_name()
