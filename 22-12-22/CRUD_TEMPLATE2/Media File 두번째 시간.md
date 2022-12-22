Static 이미지 -> 개발자가 서버에 미리 업로드 시켜놓은 것

Media 이미지 -> "사용자"가 서버에 업로드 시키는 것



# Media File

사용자가 웹에서 업로드하는 "정적 파일" (유저가 업로드하는 모든 정적 파일)



-> Image Filed (실제로 이미지 들어오는게 x) -> "**문자열**" -> 최대 100자 문자열 max_length사용해

변경 가능



** 사용하려면 반드시 Pillow 라이브러리 설치 필요 -> "error"가 계속 나타날 것



FileField() -> "파일 업로드에 사용하는 모델 필드"

2개의 매개변수를 가짐 -> upload_to, stroage

---



upload_to -> 업로드할 디렉토리와 파일 이름을 설정하는 2가지 방법

1. "문자열 / 경로"
2. 함수 호출



문자열 / 경로 방식

```python
upload_to="images/"

upload_to="images/%Y/%m/%d"
```



*반드시 2개의 인자

함수 호출(instance, filename)

instance -> FileFiled가 정의된 모델 인스턴스

대부분 이 객체는, DB에 저장되기 전이라 PK를 얻을 수 없음



filename => 기존 파일에 제공된 이름



```python
def articles_image_path(instance, filename):
    return f'image_{instance.pk}/{filename}'


class Article(models.Model):
    image = models.ImageField(upload_to=articles_image_path)
```



### blank (model 어디서든 들어올 수 있는 옵션)

기본값 : False



True인경우, 필드를 비워둘 수 있음 -> DB에 "빈 문자열"

is_Valid에서 비어있는 필드는 통과 x -> blank=True 비어있어도 통과o



vs



### Null (model 어디서든 들어올 수 있는 옵션)

기본값 : False

True인경우, django 빈값에 대해 DB -> NULL



주의사항

CharField , TextField -> **문자열 기반** 필드에는 사용하는것을 피해야 함

" ", NULL 두개가 올 수 있기때문에 중복되기 때문에 이런경우 blank True를 사용하는것을 규칙

```python
class Person(models.Model):
	name = models.CharField(max_length=10, blank=True) -> O
    
    bio = models.TextField(max_length=50, NULL=True) -x 
    
    birth_day = models.DateTimeField(NULL = True) -o
    birth_day = models.DateTimeField(blank= = True)
    
    
```



---

Media File을 저장하고 출력하기 위한 세팅

1.settings.py -> **MEDIA_ROOT, MEDIA_URL** 설정

2.upload_to 속성을 정의하여 업로드된 파일에 사용할 **MEDIA_ROOT** 하위 경로 지정

3.업로드 된 파일의 경로는 django가 **"url"** 속성을 통해 얻을 수 있음



```python
settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```

사용자가 업로드 "한" 파일을 보관할 폴더의 '절대경로'

django는 성능을 위해서 파일은 db에 저장 x

-> db에 저장되는 것은 그 저장된 "파일의 경로" -> 문자열로

[주의 할점, 많이 틀리시는 부분]STATIC_URL & MEDIA_URL을 같은경로 XXXX

```python
MEDIA_URL = '/media/'
```

MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL

업로드된 파일의 주소(URL)로 만들어주는 역할

비어있지 않은 값으로 설정한다면, **반드시 (/) 슬래쉬로 끝나야함**

[주의 할점, 많이 틀리시는 부분]MEDIA_URL / STATIC URL과 다른 경로

---

https://docs.djangoproject.com/en/4.1/howto/static-files/ 또는

구글 검색창 how to manage static files in django 입력

## Serving static files during development

의 내용 복사



예시)

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



---

form태그의 인코딩변경



articles/create.html

```python
<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
```





### 이미지 업로드시 form태그의 enctype(인코딩) 속성

1. 기본값 application/x-www-form-urlencoded (모든 문자 인코딩)

2. multipart/form-data (파일/이미지 업로드시 반드시 사용해야함)

   2-1 <input type="file"> 사용할 경우 사용

3. text/plain 인코딩 하지 않은 문자 상태로 전송 (공백 -> '+')



### img태그의 accept 속성

입력 허용할 파일 유형을 나타내는 문자열

구분된 "고유 파일 유형 지정자" -> **파일을 검증하는 하는 x**



article / views.py

```python
form = ArticleForm(request.POST,request.FILES)
```

request.FILES추가



---

### 이미지 수정



이미지 -> 데이터의 덩어리 -> 텍스트처럼 "**일부만 변경이 불가능"**



"hello wolrd" -> "hell wolrd"

-> 새로운 사진을 덮어 씌움



UPDATE.HTML

```\
<form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
```

views.py

```python
form = ArticleForm(request.POST,request.FILES,instance=article)
```

---

