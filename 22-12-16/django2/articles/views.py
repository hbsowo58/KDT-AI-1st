from django.shortcuts import render

# Create your views here.
def index(reqeust):
  return render(reqeust, 'index.html')

def hello(request):

  # context = {
  #   "name" : name
  # }

  return render(request, 'test.html')