from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserCreationForm inherits from ModelForm class
# It has 3 fields: username, password1, and password2
class registerUserForm(UserCreationForm): 
    # Here we add the email field to our user registration form model.
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        field = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        # commit = False, Returns a model object which we then add our own fields to after before commiting to database
        # Grabs the email from the form, along with 
        user = super(registerUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # Here we save the created user object after adding the email data
        if commit:
            user.save()
        return user