from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import newBookForm, EditItemForm
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

def bookOverview(request, id):
    context = {}
    book = Book.objects.get(user_id=request.user.id, id=id)
    context = {'book': book}
    initial_dict = {
        "title": book.title,
        "author": book.author,
        "complete": book.title,
        "image": book.image,
        "first_point": book.first_point,
        "second_point": book.second_point,
        "third_point": book.third_point
    }
    context['form'] = EditItemForm(initial=initial_dict)
    return render(request, 'bookDashboard/bookOverview.html', context = context)
