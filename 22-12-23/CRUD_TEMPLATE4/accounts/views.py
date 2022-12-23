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

#회원가입 양식
from django.contrib.auth.forms import UserCreationForm


# 회원수정 양식

from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm


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

def signup(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else :
        form = UserCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        # 주의할점 (탈퇴 후 -> 로그아웃 순서로 진행할것 !)
        # 주의할점 (로그아웃 후 탈퇴 xxx)
    return redirect('articles:index')



@require_http_methods(['GET', 'POST'])
def update(request):
    
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else :
        form = CustomUserChangeForm(instance = request.user)
    context = {
        "form" : form
    }
    return render(request, "accounts/update.html", context)