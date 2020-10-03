from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=256, default='')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=False, default='', blank=True)
