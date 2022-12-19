from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
  articles = Article.objects.all()

  context = {
    'articles' : articles
  }

  return render(request, 'articles/index.html', context)

def new(request):
  return render(request, 'articles/new.html')


def create(reqeust):
  return render(reqeust, 'articles/create.html')