from django.shortcuts import render, redirect
from . import models

def root(request):
    return redirect('/books')

def books(request):
    return render(request, 'books.html')

def addBook(request):
    models.addBook(request)
    return redirect ('/')

def listBook(request):
    context={
        'all_books': models.show_all_books()
    }
    return render(request, 'booklist.html', context)

def book_details(request, id):
    context={
        'specific_book':models.Books.objects.get(id=id),
        'all_authors': models.show_all_authors(),
        'all_books': models.show_all_books()
    }
    return render (request,"bookdetails.html",context)

def author(request):
    context={
        'all_authors': models.show_all_authors()
    }
    return render(request,'author.html',context)
