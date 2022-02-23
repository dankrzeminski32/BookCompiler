from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import newBookForm
from django.shortcuts import redirect
from .models import Book
# Create your views here.


def userView(request):
    print(Book.objects.filter(user__id=request.user.id))
    context = {}
    if request.method == "POST":
        form = newBookForm(data=request.POST, user=request.user, image=request.FILES.get('image','book_pics/default.jpg'))
        if form.is_valid():
            form.save()
            return redirect('dashboardView')
    else:
        form = newBookForm()
        context['form'] = newBookForm()
        context['userBooks'] = Book.objects.filter(user_id=request.user.id)
    return render(request, 'bookDashboard/userDashboard.html', context)