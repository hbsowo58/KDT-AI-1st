from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path("", views.index, name="index"),
    # path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete', views.delete, name="delete"),
    # path('<int:pk>/edit', views.edit, name="edit"),
    path('<int:pk>/update', views.update, name="update"),
    path("test/", views.test, name="test"),
    path("test/<int:pk>", views.test2, name="test2"),
]
