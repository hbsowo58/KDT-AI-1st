from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login(request):
    
    form = AuthenticationForm(request, request.POST)
    
    if form.is_valid():
        #로그인을 시켜라
        auth_login(request, form.get_user())
        return redirect("articles:index")

    else:
        form = AuthenticationForm()
    context = {
    'form' : form
    }
    return render(request, 'accounts/login.html',context)