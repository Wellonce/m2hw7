from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, BookGenre, User


class BookListView(ListView):
    model = Book
    template_name = "books/book-list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    slug_url_kwarg = 'slug'
    template_name = "books/book-detail.html"
    context_object_name = "book"

class GenreView(ListView):
    model = BookGenre
    template_name = "books/genre.html"
    context_object_name = "genres"

class GenreDetailView(DetailView):
    model = BookGenre
    template_name = "books/genre-detail.html"
    context_object_name = "genre"



class AuthorView(DetailView):
    model = User
    template_name = 'book/author.html'
    