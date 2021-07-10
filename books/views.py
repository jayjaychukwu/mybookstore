from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
def index(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'books/list.html', context)

def add(request):
    form = addbookform()
    if request.method == 'POST':
        form = addbookform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'books/addbook.html', context)

def book_list(request):
    book = Book.objects.all()
    f = bookfilter(request.GET, queryset=book)
    return render(request,'books/search.html', {'filter':f})

