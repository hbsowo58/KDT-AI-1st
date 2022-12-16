프로젝트 시작 과정

1.가상환경을 생성한다
pyhon -m venv [가상환경 명]

ex) python -m venv venv

2.가상환경을 실행한다

source [가상환경 명] / Scripts / activate

3.장고를 설치한다

pip install django~=3.2.10

4.프로젝트를 생성한다

django-admin startproject [프로젝트 명] . [옵션 여부]

ex)django-admin startproject crud .

5.서버를 실행한다

"manage.py가 있는 경로에서"

python manage.py runserver

6. 애플리케이션을 만든다

python manage.py startapp [애플리케이션 이름] 복수형권장

ex) python manage.py startapp articles

7 프로젝트의 settings.py에 install_app에 추가

INSTALLED_APPS = [
    '애플리케이션이름',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

---

데이터의 흐름에 따라서, index.html 띄우기

URL에

http://127.0.0.1:8000/[입력되면]

-> "프로젝트" urls.py에 접근

<!-- path('admin/', admin.site.urls), -->
위의 형식을 참고하면 path라는 함수

<!-- /admin 이라는 요청이 왔을떄-->

<!-- ex) http://127.0.0.1:8000/admin -->

뒤의 콜백함수를 실행한다 여기서는 admin.site.urls

콜백함수를 urls.py에 작성할 수 x

함수 -> views.py

애플리케이션 -> views를 작성 (template이 필요)

애플리케이션 -> templeats라는 폴더 -> 랜더링할 파일을 생성