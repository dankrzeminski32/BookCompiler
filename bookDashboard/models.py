from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class bookList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookList')

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class book(models.Model):
    bookList = models.ForeignKey(bookList, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    complete = models.BooleanField()

    def __str__(self):
        return self.title

