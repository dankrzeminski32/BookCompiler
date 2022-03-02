from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import registerUserForm, UpdateProfile
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate #add this


# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = registerUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginView')
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
                return redirect("home")
            else:
                # messages.error invalid username or password (remove http response)
                return HttpResponse("Invalid username or password")
        else:
            #Form is not valid, messages.error(request,'invalid username or pass)
            return HttpResponse("Invalid username or password")
    form = AuthenticationForm()
    return render(request = request, template_name = "userManagement/login.html", context = {"login_form": form})

def logoutUser(request):
    logout(request)
    return redirect('home')


def userProfile(request):
    args = {}
    instanceVariables = {
        'username': request.user.username,
        'email': request.user.email
    }

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form = UpdateProfile(instanceVariables)

    args['form'] = form
    print(form)
    return render(request, 'userManagement/profile.html', args)
    