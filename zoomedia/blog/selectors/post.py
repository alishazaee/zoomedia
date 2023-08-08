from django.db.models import QuerySet
from ..models import Post
from django.contrib.auth import get_user_model


def post_detail(*, slug:str, user:get_user_model()) -> Post: 
    return Post.objects.get(slug=slug, author=user)

