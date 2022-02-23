from django import forms
from django.forms import ModelForm
from bookDashboard.models import Book

class newBookForm(ModelForm):
    def __init__(self, **kwargs):
        self.user = kwargs.pop('user', None)
        self.image = kwargs.pop('image', None)
        super(newBookForm, self).__init__(**kwargs)
        self.fields['title'].required = True
        self.fields['author'].required = True
        self.fields['complete'].required = True
    
    def save(self, commit=True):
        obj = super(newBookForm,self).save(commit=False)
        obj.user = self.user
        obj.image = self.image
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Book
        fields = ['title','author','complete','image']