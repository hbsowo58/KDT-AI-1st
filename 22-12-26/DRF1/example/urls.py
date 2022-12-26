from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.HelloAPI),
    path("fbv/books", views.booksAPI),
    path("fbv/book/<int:bid>", views.bookAPI),
]
