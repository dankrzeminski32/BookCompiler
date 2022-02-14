from django import forms
from django.forms import ModelForm
from bookDashboard.models import book

class newBookForm(ModelForm):
    def __init__(self, **kwargs):
        self.user = kwargs.pop('user', None)
        super(newBookForm, self).__init__(**kwargs)
    
    def save(self, commit=True):
        obj = super(newBookForm,self).save(commit=False)
        obj.user = self.user
        if commit:
            obj.save()
        return obj

    class Meta:
        model = book
        fields = ['title','complete']