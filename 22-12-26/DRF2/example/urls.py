from django.urls import path
from . import views
from .views import BooksAPI, BookAPI

urlpatterns = [
    path("hello/", views.HelloAPI),
    path("fbv/books", views.booksAPI),
    path("fbv/book/<int:bid>", views.bookAPI),
    path("cbv/books", BooksAPI.as_view()),
    path("cbv/book/<int:bid>", BookAPI.as_view()),
]
