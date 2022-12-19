# 복습

프로젝트 생성과정 1~6 실행



models.py 작성



-> make migrations

-> python manage.py migrate



라이브러리 설치

pip install ipython

pip install django-extensions



settings.py -> install app



```python
INSTALLED_APPS = [
    'articles',

    'django_extensions',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

쉘 실행

```
python manage.py shell_plus
```



CRUD 작업 실행



CREATE

3가지 방법

```
1) 생성자 함수 호출 후 저장

In [2]: article = Article()

In [3]: article.title = "first"

In [4]: article.content = "django!"

In [5]: article.save()

2)초기값과 함께 인스턴스 생성후 저장

In [6]: article = Article(title="second", content ="django!!")   

In [7]: article.save()

3) QuerySet API - create메소드   1,2와는 다르게 저장하지 않아도됨

In [8]: Article.objects.create(title="third", content="django!!!")
```



save()

객체를 DB에 저장함

데이터 생성을 해도 save()를 호출하지 않으면 db에 반영되지 않음

모델의 인스턴스를 생성한 후, 반드시 save() 호출



```python
모델 완성
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title;
```



```
python manage.py makemigrations
```

