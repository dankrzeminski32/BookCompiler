from django import forms
from django.forms import ModelForm
from bookDashboard.models import book

class newBookForm(ModelForm):
    class Meta:
        model = book
        fields = ['title','complete','user']