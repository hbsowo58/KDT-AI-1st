from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.index),
    path('hello/', views.hello, name="hello"),
]