from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import newBookForm
from django.shortcuts import redirect
from .models import book
# Create your views here.


def userView(request):
    print(book.objects.filter(user__id=request.user.id))
    context = {}
    if request.method == "POST":
        form = newBookForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboardView')
    else:
        form = newBookForm()
        context['form'] = newBookForm()
        context['userBooks'] = book.objects.filter(user_id=request.user.id)
    return render(request, 'bookDashboard/userDashboard.html', context)