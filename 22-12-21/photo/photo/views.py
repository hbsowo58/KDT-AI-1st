from django.shortcuts import render, get_object_or_404
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all()
    context = {
        "photos" : photos
    }
    # 데이터를 가져와서
    # context photos
    return render(request, 'photo/photo_list.html',context)

def photo_detail(request, pk):
    # photo = Photo.objects.get(pk = pk)
    # 예시 : http://127.0.0.1:8000/detail/7로 방문하면 (7이 없다는 가정) DoesNotExist error
    
    # get_object_or_404(클래스, pk = 옵션)
    photo = get_object_or_404(Photo, pk = pk)
    
    # 데이터를 못가져왔을시, Page not found (404)
    
    context = {
        "photo" : photo
    }
    return render(request, 'photo/photo_detail.html', context)

def photo_post(request):
    
    form = PhotoForm()
    
    context = {
        "form" : form
    }
    
    return render(request, 'photo/photo_post.html',context)