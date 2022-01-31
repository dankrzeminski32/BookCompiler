from django.shortcuts import render
from django.http import HttpResponse
from .forms import registerUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate #add this


# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = registerUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>YOU SUCCESSFULLY REGISTERED</h1>")
    else:
        form = registerUserForm()
    return render(request, 'userManagement/register.html', {'form': form})

def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                #redirect and messages.info
                return HttpResponse(f"Successfully logged in as{username}")
            else:
                # messages.error invalid username or password (remove http response)
                return HttpResponse("Invalid username or password")
        else:
            #Form is not valid, messages.error(request,'invalid username or pass)
            return HttpResponse("Invalid username or password")
    form = AuthenticationForm()
    return render(request = request, template_name = "userManagement/login.html", context = {"login_form": form})