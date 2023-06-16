from contextlib import redirect_stderr
from multiprocessing.dummy import active_children
from urllib import request
from django.shortcuts import render , redirect, get_object_or_404
from . models import *
from .forms import *

# Create your views here.

def books(request):


    context = {
        'categry':Category.objects.all() ,
        'books': Books.objects.all(),
        'bookforms': Bookforme(),
        

    }
    return render(request,'pages/books.html',context)

def index(request):

    # carate if for save book in frontend ___
    if request.method == 'POST':
        add_book = Bookforme(request.POST , request.FILES)
        if add_book.is_valid(): # if this deta ture your saved
            add_book.save()


    # carate if for save categery
    if request.method == 'POST':
        add_cat = Categeryforme(request.POST)
        if add_cat.is_valid(): # if this deta ture your saved
            add_cat.save()


    context = {
        'categry':Category.objects.all() ,
        'books': Books.objects.all(),
        'bookforms': Bookforme(),
        'categery' : Categeryforme(),
        'allbook':Books.objects.filter(active=True).count(),
        'booksold':Books.objects.filter(status = 'sold').count(),
        'bookrental':Books.objects.filter(status = 'rental').count(),
        'bookavailble':Books.objects.filter(status = 'availble').count(),


    }
    return render(request,'pages/index.html',context)

def delete(request,id):
    delete_book = get_object_or_404(Books,id=id)
    if request.method == 'POST':
          delete_book.delete()
          return redirect('/')
   
    return render(request,'pages/delete.html')


def delete1(request,id):
    delete_book = get_object_or_404(Books,id=id)
    if request.method == 'POST':
          delete_book.delete()
          return redirect('/books')
   
    return render(request,'pages/delete.html')


def update(request,id):
    
    book_id = Books.objects.get(id=id)
    if request.method ==  'POST':
       book_save = Bookforme(request.POST,request.FILES,instance=book_id)
       if book_save.is_valid:
          book_save.save()
          return redirect('/books') 

    else:
        book_save = Bookforme(instance=book_id)

    context = {
        'form':book_save,
    }
    return render(request,'pages/updata.html',context)



def faces(request):
    
    if request.method == 'POST':
        add_book = Bookforme(request.POST , request.FILES)
        if add_book.is_valid(): # if this deta ture your saved
            add_book.save()


    context = {
        'admin1': Categeryforme(),
        'admin2':Bookforme(),
    }
    return render(request , 'faces.html',context)
