from django.db import models
from zoomedia.common.models import BaseModel
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

class Post(BaseModel):
    author= models.ForeignKey(get_user_model(), on_delete=models.CASCADE ,related_name='author')
    slug = models.SlugField(max_length=255 , primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2024)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
    
    
