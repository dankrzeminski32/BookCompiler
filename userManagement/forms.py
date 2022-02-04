from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# UserCreationForm inherits from ModelForm class
# It has 3 fields: username, password1, and password2
class registerUserForm(UserCreationForm): 
    # Here we add the email field to our user registration form model.
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None
        }


    def save(self, commit=True):
        # commit = False, Returns a model object which we then add our own fields to after before commiting to database
        # super() Grabs all of the data from the class in our MRO (UserCreationForm). 
        # This does not include email, so we have to add it after
        user = super(registerUserForm, self).save(commit=False)
        # self is referring to our form object so  we access it's cleaned data attribute for 'email'
        user.email = self.cleaned_data['email']
        # Here we save the created user object after adding the email data
        if commit:
            user.save()
        return user