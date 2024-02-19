from django.urls import path

from apps.books.views import BookListView, BookDetailView, GenreView, GenreDetailView, AuthorView

app_name = "books"

urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book-detail"),
    path('genres/', GenreView.as_view(), name="genre-page"),
    path('genres-detail/<int:pk>', GenreDetailView.as_view(), name="detail-page"),
    path('author/<int:pk>', AuthorView.as_view(), name="author"),
]
