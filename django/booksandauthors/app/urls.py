from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('books', views.books),
    path('addbook', views.addBook),
    path('booklist', views.listBook),
    path('addauthor', views.author),
    path('books/<int:id>', views.book_details),
    path('authorlist', views.author_details)
    ]