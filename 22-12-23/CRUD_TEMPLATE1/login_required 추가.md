### 인증과 권한(로그인/로그아웃/회원가입)



장고의 인증 시스템

django.contrib.auth , contrib 모듈에 들어있음



```python
'django.contrib.auth',
'django.contrib.contenttypes',
```

장고에서는 이미 인증권한 관련된 라이브러리를 설치해두었음

django.contrib.auth -> 인증 프레임워크 핵심과 기본 모델

django.contrib.contenttypes-> 사용자가 "생성한" 모델에 권한 연결할 수 있음



인증(Authentication) ->  신원 확인 / 사용자가 자기가 누군지 확인

권한(Authorization) -> 권한 (부여) /인증된 사용자가 할 수 있는 작업을 결정

---

애플리케이션 생성

```python
python manage.py startapp [애플리케이션 이름]

python manage.py startapp accounts
```

반드시 애플리케이션 명이 accounts일 필요는 x

인증과 django 내부적으로는 accounts을 사용을 하도록 권장



```python
INSTALLED_APPS = [
    'articles',
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**프로젝트** / urls.py



```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]

```

accounts / urls.py



```
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [

]

```





---

# HTTP의 특징 2가지



1.비연결지향(connectionless)

서버는 요청에 대한 응답을 보낸후, 연결을 끊음

2.무상태(stateless)

연결을 끊는순간 클라이언트 / 서버간의 통신이 상태 정보가 유지되지 x

클라이언트가 서버랑 주고받는 메시지는 모두다 독립적



### 클라이언트와 서버의 지속적인 관계 유지를 위해 쿠키와 세션



쿠키 : 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

서버에 방문하면, 클라이언트에 설치되는 작은 기록 파일

[참고] 쿠키를 해킹하면, 악성코드를 설치 시키거나 해당 사용자의 계정 접근 권한 획득할 수 있음


http 쿠키 -> 상태가 있는 세션 만듦



쿠키는 두요청이 동일한 브라우저에 들어왔는지 아닌지를 판단



**웹페이지에 접속을하면, 쿠키를 저장, "같은 고객"이 서버에 "재요청"하면, 쿠키와 함께 전송**

---

**쿠키의 사용 목적**

1. 세션 관리 (로그인 유지, 아이디 자동완성, 공지 하루안보기, 팝업체크, 장바구니)

  2.개인화 (개인이 검색, 개인이 선호하는 색상 컨텐츠)

3.트래킹(사용자의 행동을 기록 & 분석)



---

세션

사이트와 고객(클라이언트)간에 연결 유지 상태(STATE)를 유지 시키는 것



클라이언트가 서버에 접속하면, 특정 session id를 발급하고, 클라이언트는

session id를 쿠키에 저장



클라이언트가 "다시" 서버에 요청하게 되면, 쿠키와 함께 "서버로" 전달

쿠키는 요청때마다 서버에 함께 전송

-> ID는 세션을 구별하기 위해 필요 쿠키는 ID만 저장

---

쿠키의 수명(두가지)

1. 세션 쿠키 : 현재 브라우저가 종료되는 순간 삭제 -> 로그아웃 하거나 브라우저를 끌때까지는

   로그인 상태가 유지

2.특정 시간이 정해진 쿠키 (그 시간까지만 접속이 유지됨 -> )

---

**장고에서의 세션**

django_session이라는 테이블

모든 것을 세션으로 처리하면 되겠네? -> 세션 DB에 저장되기때문에

모든것을 세션처리하면 DB가 과부하

```python
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
```

----

## 로그인

Session Create 하는 과정과 같음 -> 인증을 위한 내장 함수

AuthenicationForm (사용자 로그인을 위한 Form) request를 첫번째 인자로 취함

**login함수**



login(request, user, backend=None)

현재 세션에 연결하려는 인증된 사용자가 있는 경우 login 함수가 필요

사용자가 로그인하면, view함수에서 사용됨

HttpRequest객체와 User객체가 필요



accounts/urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name="login"),
]

```

accounts/views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(['GET', 'POST'])
def login(request):
    
    if request.method == 'POST':
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
```

---



get_user란? AuthenticationForm -> 메서드로 정의되어있어서 자체 호출가능



```python
class AuthenticationForm(forms.Form):
    
    
    def get_user(self):
        return self.user_chache
```



---

templates/가장 최상단의 base.html (모든 템플릿 상속을 해줌)



```html
  <div class="container">
    <a href="{% url 'accounts:login' %}">Login</a>
    {% block content %}
    {% endblock content %}
  </div>
```

---

템플릿에 인증, 유저 정보를 출력해보자



프로젝트의 base.html



```html
  <div class="container">
    <h3>안녕하세요 {{ user }} 님</h3>
    <a href="{% url 'accounts:login' %}">Login</a>
    {% block content %}
    {% endblock content %}
  </div>
```

입력하지 않은 user가 화면에 잘 출력됨

---



settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

장고가 내장으로, context를 만들어서 사용하고 있다

{{user}}에 대한 정보 , 익명의 유저 등은 django.contrib.auth.context_processors.auth에 존재



---

# 로그 아웃

**logout**(request)

HttpRequest를 객체 인자로 받습니다 -> 반환값이 없음

사용자가 로그인하지 않은경우 -> 에러를 발생시키지 않음

"현재" (로그인 된 시점)의 유저가 로그아웃 요청을 하면,

session id를 DB에서 완전 삭제, 클라이언트의 쿠키에서도 sessionid 삭제



accounts/urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]

```

accounts / views.py



```python
# 로그아웃에 필요
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST


@require_POST
def logout(request):
    auth_logout(request)
    return redirect("articles:index")
```

---

**사용자에 대한 접근 제한**



2가지 방법

is_autgenticated attribute

login_required decorator



**is_autgenticated** 

user model 속성 1개



django.contrib.auth.middleware.AuthenticationMiddleware를 통과했는지를 검사



base.html

```html
{% if request.user.is_authenticated %}
<h3>안녕하세요 {{ user }} 님</h3>

<form action = "{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
</form>
{% else %}
<a href="{% url 'accounts:login' %}">Login</a>
{% endif %}
```



---

accounts / views.py



```python
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect("articles:index")
    
    
    if request.method == 'POST':
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
    
    
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("articles:index")   
```



articles/index.html

```
{% if request.user.is_authenticated %}
<a href="{% url 'articles:create' %}">[CREATE]</a>

{% else %}
<a href="{% url 'accounts:login' %}">[게시글을 작성하려면, 로그인 하세요]</a>
{% endif %}
```



---

**login_required decorator**



사용자가, 로그인되어있지 않으면 settings.LOGIN_URL에 설정된

문자열 기반 경로로 REDIRECT



-> 기본값은 : **'/accounts/login/'**



-> 사용자가 로그인된 경우에는 정상적으로 view함수 실행

-> 인증에 성공시 사용자가 redirect되어야 하는 경로는 **"next"라는 쿼리 문자열**

매개변수에 저장됨



**예시) /accounts/login/?next=/articles/create/**



next -> 로그인이 정상적으로 진행되면, 기존에 요청했던 주소로 redirect 시키기 위해서

주소를 보관(키핑)



단, 별도로 처리를 해주지 않으면 우리가 view 설정한 redirect경로로 이동하게 됨

