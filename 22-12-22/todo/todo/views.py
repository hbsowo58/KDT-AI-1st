from django.shortcuts import render
from .models import Todo
# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todo_list.html',context)