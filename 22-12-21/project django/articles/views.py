from django.shortcuts import render, redirect , get_object_or_404
from .models import Article
from .forms import ArticleForm

from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
  articles = Article.objects.all()

  # articles = Article.objects.order_by('-pk')
  # articles = Article.objects.order_by('-id')
  # 'db에서' 내림차순으로 해서 가져와 화면에 출력

  # articles = Article.objects.all()[::-1]
  # db에서 가져와서 '파이썬'으로 내림차순으로 변경해서 출력

  context = {
    'articles' : articles
  }

  return render(request, 'articles/index.html', context)

# def new(request):
#   form = ArticleForm()
  
#   context = {
#     'form' : form
#   }
  
#   return render(request, 'articles/new.html', context)
@ require_http_methods(['GET', 'POST'])
def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
    
      # form.save()
      # return redirect('articles:detail', form.pk)
      # 1번방법
    
      article = form.save()
      return redirect('articles:detail', article.pk)
      # 2번방법
  else :
    form = ArticleForm()
    
  context = {
    'form' : form
  }
      
  return render(request, 'articles/create.html', context)

@require_safe
def detail(request,pk):


  # 클래스명.objects.QuestAPI
  # article = Article.objects.get(pk=pk)
  # articles = Article.objects.all()
  
  # get_object_or_404(1,2) -> 첫번째 매개변수 1: 클래스 2, pk 구분자
  article = get_object_or_404(Article, pk=pk)

  context = {
    'article' : article
  }


  return render(request, 'articles/detail.html', context)


@require_POST
def delete(request,pk):
  # article = Article.objects.get(pk = pk)
  article = get_object_or_404(Article, pk=pk)

  # if request.method == 'POST': -> 데코레이터가 있기때문에 POST를 검사하지 않아도 됨
  article.delete()
  return redirect('articles:index')
    # return render(request, 'articles/index.html')
  # return redirect('articles:detail', article.pk)

# def edit(request,pk):
#   article = Article.objects.get(pk=pk)

#   context = {
#     "article" : article
#   }
  
#   return render(request,'articles/edit.html',context)

@require_http_methods(['GET','POST'])
def update(request, pk):
  # article = Article.objects.get(pk = pk)
  article = get_object_or_404(Article, pk=pk)
  if request.method == "POST":
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
  else:
    form = ArticleForm(instance=article)
  context = {
    'form' : form ,
    'article' : article
  }
  return render(request,'articles/update.html',context)

# def test(request):
#   # return render(request, "articles/test.html")
#   # 랜더가 없을떄 위의 코드를 대체하는 방법
#   template = loader.get_template('articles/test.html')
  
  
#   # template.render(1,2)
#   # 1번 자리 -> dic
#   # 2번 자리 -> request
  
#   return HttpResponse(template.render({},request))

def test(request):
  # print(request)
  return render(request, "articles/test.html")
  

# get_object_or_404()가 없으면
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