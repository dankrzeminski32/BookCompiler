from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def userView(request,id):
    context = {}
    if request.method == 'GET':
        user = User.objects.get(id=id)
        context = {'userProfile': user}
        return render(request, 'bookDashboard/user.html', context )
    return HttpResponse("<h1>INVALID USER</h1>")