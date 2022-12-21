from django import forms
from .models import Photo

# Create your models here.
class PhotoForm(forms.ModelForm):
    class Meta:
        # 어디로부터 가져올 것인가?
        model = Photo
        fields = '__all__'
        # exclude
    
