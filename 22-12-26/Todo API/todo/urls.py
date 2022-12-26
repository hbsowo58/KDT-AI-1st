from django.urls import path
from .views import TodosAPIView


urlpatterns = [
    path('todo', TodosAPIView.as_view()),
]
