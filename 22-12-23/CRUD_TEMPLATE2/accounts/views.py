from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
# 로그인에 필요

# 로그아웃에 필요
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST

# login_required
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect("articles:index")
    
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            #로그인을 시켜라
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or "articles:index")

    else:
        form = AuthenticationForm()
    context = {
    'form' : form
    }
    return render(request, 'accounts/login.html',context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("articles:index")