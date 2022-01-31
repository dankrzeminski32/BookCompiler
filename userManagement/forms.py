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

# class loginForm(AuthenticationForm):
#     username = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control'}))
#     password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password'}))

#     remember_me = forms.BooleanField(required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'remember_me']