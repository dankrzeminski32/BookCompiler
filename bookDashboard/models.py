from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
 #   author = models.CharField(max_length=100)
    complete = models.BooleanField()
    image = models.ImageField(default='book_pics/default.jpg', upload_to='book_pics')

    def __str__(self):
        return self.title

