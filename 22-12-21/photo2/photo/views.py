from django.shortcuts import render, get_object_or_404, redirect
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
    # print(request.POST)
    # POST 요청일때만 
    
    if request.method == "POST":
        # 데이터가 정상적으로 입력되었을때
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
        # 데이터를 저장
        return redirect('photo_detail', pk = photo.pk)
        # 저장후, detail페이지로 "그 입력된 아이디 번호와"
    else :
        form = PhotoForm()
        
        
    context = {
        "form" : form,
        "title" : "New Photo"
    }
    
    return render(request, 'photo/photo_post.html',context)

def photo_edit(request,pk):
    photo = get_object_or_404(Photo, pk=pk)
    # photo_post와 비슷
    
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():    
            form.save()
            return redirect('photo_detail', pk = photo.pk)
        # 데이터를 1개 가져올 것, instance 키워드를 사용하면 (수정 = update)
    else:
        form = PhotoForm(instance=photo)
            
    context = {
        "form" : form,
        "title" : "Edit Photo"
    }
    
    return render(request, 'photo/photo_post.html', context)