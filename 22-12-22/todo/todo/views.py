from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todo_list.html',context)

def todo_detail(request, pk):
    # todo = Todo.objects.get(id=1)
    todo = Todo.objects.get(pk=pk)
    context = {
        "todo" : todo
    }
    return render(request, 'todo_detail.html', context)

def todo_post(request):
    # print(request.POST)
    form = TodoForm(request.POST)
    
    if form.is_valid():
        form.save()
        
        return redirect("todo_list")
    
    context = {
        "form" : form
    }
    
    return render(request, 'todo_post.html',context)