from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    name = models.CharField(max_length=512)
    author = models.CharField(max_length=256)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class UserBookAllocation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
