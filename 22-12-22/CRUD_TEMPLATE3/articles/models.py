from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    
    image_thumbnail = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(200,300)],
        format="JPEG",
        options={'quality': 90}
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
