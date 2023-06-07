from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Books, related_name='books')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

def show_all_authors():
    return Authors.objects.all()

def show_all_books():
    return Books.objects.all()

def addBook(request):
    newBook = Books.objects.create(title=request.POST['title'], desc=request.POST['description'])
    return newBook

def show_all_authors():
    return Authors.objects.all()

def show_all_books():
    return Books.objects.all()

def create_author(request):
	new_author = Authors.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
	return new_author

def addAuthor(request):
    this_book = Books.objects.get(id=int(request.POST['author_to_book']))
    this_publisher = Authors.objects.get(id=int(request.POST['atob']))
    this_book.authors.add(this_publisher)
