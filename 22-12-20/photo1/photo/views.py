from django.shortcuts import render
from .models import Photo

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
    photo = Photo.objects.get(pk = pk)
    context = {
        "photo" : photo
    }
    return render(request, 'photo/photo_detail.html', context)