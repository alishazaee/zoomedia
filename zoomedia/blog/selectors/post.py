from django.db.models import QuerySet
from ..models import Post
from django.contrib.auth import get_user_model
from ..filters import FilterPost

def post_detail(*, slug:str, user:get_user_model()) -> Post: 
    return Post.objects.get(slug=slug, author=user)

def post_list(*, filters=None , user:get_user_model()):
    filters = {} or filters
    query = Post.objects.all()
    return FilterPost(filters , query).qs