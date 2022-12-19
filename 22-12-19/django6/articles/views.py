from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
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

def new(request):
  return render(request, 'articles/new.html')

def create(request):


  title = request.POST.get('title')
  content = request.POST.get('content')
  # print(request)

  article = Article()
  article.title = title
  article.content = content
  article.save()
  # 1번

  # article = Article(title=title,content=content)
  # article.save()
  # 2번

  # Article.objects.create(title=title, content=content)
  # 3번

  # return render(request, 'articles/create.html')
  # return redirect('articles:index')
  return redirect('articles:detail', article.pk)

def detail(request,pk):


  # 클래스명.objects.QuestAPI
  article = Article.objects.get(pk=pk)
  # articles = Article.objects.all()

  context = {
    'article' : article
  }


  return render(request, 'articles/detail.html', context)

def delete(request,pk):
  article = Article.objects.get(pk = pk)

  if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # return render(request, 'articles/index.html')
  else:
    return redirect('articles:detail', article.pk)

def edit(request,pk):
  article = Article.objects.get(pk=pk)

  context = {
    "article" : article
  }
  
  return render(request,'articles/edit.html',context)

def update(request, pk):
  article = Article.objects.get(pk = pk)
  article.title = request.POST.get('title')
  article.content = request.POST.get('content')
  article.save()
  return redirect('articles:detail', article.pk)