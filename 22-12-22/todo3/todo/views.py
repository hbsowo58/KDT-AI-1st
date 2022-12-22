from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def todo_list(request):
    todos = Todo.objects.filter(complete=False)
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
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else : 
        form = TodoForm()
        
    context = {
        "form" : form
    }
    
    return render(request, 'todo_post.html',context)

def todo_edit(request,pk):
    todo = Todo.objects.get(pk=pk)
    
    if request.method == "POST":
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)
    context = {
        "form" : form
    }
    return render(request, 'todo_post.html',context)

def done_list(request):
    dones = Todo.objects.filter(complete=True)
    context = {
        "dones" : dones
    }
    return render(request, 'done_list.html', context)

def todo_done(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')