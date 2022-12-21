# HTTP requests

Django에서 HTTP 요청을 처리하는 방법



1. Django shortcut functions
2. View decorators

---

django.shortcut -> 개발에 도움되는 여러 함수 / 클래스등 자체 제공

shortcut functions 종류

1.render()

2.redirect()

3.get_object_or_404()

4.get_list_or_404()



### 만약.. render라는 함수가 없다면..?



```python
from django.http import HttpResponse
from django.template import loader

def test(request):
  # return render(request, "articles/test.html")
  # 랜더가 없을떄 위의 코드를 대체하는 방법
  template = loader.get_template('articles/test.html')
  
  
  # template.render(1,2)
  # 1번 자리 -> dic
  # 2번 자리 -> request
  
  return HttpResponse(template.render({},request))
```



### render라는 함수가 존재한다면..?

```python
def test(request):
  return render(request, "articles/test.html")
```

---

get_object_or_404()

클래스에서, 어떤 데이터를 가져왔을때 (존재하지 않으면) 

기존에는DoesNotExist 

-> 위의 에러 대신에 HTTP 상태코드 404



클래스.objects.get() -> 데이터가 없는경우 -> 예외를 발생

->상태코드 500번을 나타내줌



예시 코드



```python
  # article = Article.objects.get(pk=pk)

  # get_object_or_404(1,2) -> 첫번째 매개변수 1: 클래스 2, pk 구분자
  article = get_object_or_404(Article, pk=pk)
```



-> 사용자에게 올바른 에러를 보여줄 수 있다



### 만약에 get_object_or_404를 사용하지 않는다면..?



```python
from django.http import Http404

def test2(request,pk):
  try:
    article = Article.objects.get(pk=pk)
  except Article.DoesNotExist:
    raise Http404("404에러가 발생했어요")
  
  context = {
    'article' : article
  }
  return render(request, 'articles/detail.html', context)
```

get_object_or_404()가 있을시

```python
def detail(request,pk):
  article = get_object_or_404(Article, pk=pk)
  context = {
    'article' : article
  }
  return render(request, 'articles/detail.html', context)
```



