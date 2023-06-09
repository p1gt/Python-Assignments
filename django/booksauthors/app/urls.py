from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('books', views.books),
    path('authors', views.authors),
    path('books/add', views.addBook),
    path('authors/add', views.addAuthor),
    path('books/<int:id>', views.viewBook),
    path('authors/<int:id>', views.viewAuthor),
    path('books/<int:id>/add_author', views.addAuthorToBook, name='add_author_to_book'),
    path('authors/<int:id>/add_book', views.addBookToAuthor, name='add_book_to_author'),
]