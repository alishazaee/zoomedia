from django.db.models import QuerySet
from ..models import Post
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db import transaction
from zoomedia.userprofile.services.profile import cache_profile
@transaction.atomic
def create_post(*,  user:get_user_model() , title: str , description : str) -> Post: 
    post = Post.objects.create( author=user , title = title , description=description)
    cache_profile(user=user)
    return post

def delete_post(*,  user:get_user_model() , slug : str) : 
     Post.objects.get( author=user , slug = slug).delete()
 
