from django.db import models

class book(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField('author')

class author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField('book')

def addBook(request):
    if request.method == 'POST':
        newBook = book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        newBook.save()
    return newBook

def addAuthor(request):
    if request.method == 'POST':
        newAuthor = author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
        newAuthor.save()
        return newAuthor

def addAuthorToBook(request, id):
    if request.method == 'POST':
        book_obj = book.objects.get(id=id)
        author_id = request.POST.get('author')
        author_obj = author.objects.get(id=author_id)
        book_obj.authors.add(author_obj)

def addBookToAuthor(request, id):
    if request.method == 'POST':
        author_obj = author.objects.get(id=id)
        book_id = request.POST.get('book')
        book_obj = book.objects.get(id=book_id)
        author_obj.books.add(book_obj)