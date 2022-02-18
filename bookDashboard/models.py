from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    complete = models.BooleanField()

    def __str__(self):
        return self.title

