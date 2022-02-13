from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import newBookForm
from django.shortcuts import redirect
from .models import book
# Create your views here.


def userView(request):
    print(book.objects.filter(user__pk=request.user.id))
   # context = {}
  #  context['form'] = newBookForm()
    if request.method == "POST":
        form = newBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboardView')
    else:
        form = newBookForm()
    return render(request, 'bookDashboard/userDashboard.html', {'form': form})