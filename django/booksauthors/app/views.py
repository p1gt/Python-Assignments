from django.shortcuts import render, redirect
from . import models

def root(request):
    return render(request, 'root.html')

def books(request):
    data = {'books': models.book.objects.all()}
    return render(request, 'books.html', data)

def authors(request):
    data = {'authors': models.author.objects.all()}
    return render(request, 'authors.html', data)

def addBook(request):
    newBook = models.addBook(request)
    return redirect(f'/books/{newBook.id}')

def addAuthor(request):
    newAuthor = models.addAuthor(request)
    return redirect(f'/authors/{newAuthor.id}')

def viewBook(request, id):
    data = {'book': models.book.objects.get(id=id),
            'all_authors': models.author.objects.all()
        }
    return render(request, 'viewbook.html', data)

def viewAuthor(request, id):
    data = {'author': models.author.objects.get(id=id),
            'all_books': models.book.objects.all()
        }
    return render(request, 'viewauthor.html', data)

def addAuthorToBook(request, id):
    models.addAuthorToBook(request, id)
    return redirect(f'/books/{id}')

def addBookToAuthor(request, id):
    models.addBookToAuthor(request, id)
    return redirect(f'/authors/{id}')