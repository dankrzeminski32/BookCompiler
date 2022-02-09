from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.


def userView(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'bookDashboard/userDashboard.html', context )
    return HttpResponse("<h1>INVALID USER</h1>")