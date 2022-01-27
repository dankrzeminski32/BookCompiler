from django.shortcuts import render
from django.http import HttpResponse
from .forms import registerUserForm

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
