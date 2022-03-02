from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    complete = models.BooleanField()
    image = models.ImageField(default='book_pics/default.jpg', upload_to='book_pics')
    first_point_title = models.CharField(max_length=100)
    first_point = models.TextField(blank=True)
    second_point_title = models.CharField(max_length=100)
    second_point = models.TextField(blank=True)
    third_point_title = models.CharField(max_length=100)
    third_point = models.TextField(blank=True)
    is_review_complete = models.BooleanField()

    def __str__(self):
        return self.title

