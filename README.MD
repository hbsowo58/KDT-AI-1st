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