from ..models import Follow , Profile
from django.db.models import QuerySet
from django.contrib.auth import get_user_model

def get_follower_count(*, user: get_user_model())-> int:
    return Follow.objects.filter(following=user).count()

def get_following_count(*, user:get_user_model()) -> int:
    return Follow.objects.filter(follower=user).count()

def get_profile_detail(*,user:get_user_model()) -> Profile:
    return Profile.objects.get(user__username=user.username)

def get_follower(*, username:str) -> QuerySet[get_user_model()]:
    user = get_user_model().objects.get(username=username)
    follow = Follow.objects.filter(following=user)
    return follow

def get_following(*, username:str) -> QuerySet[get_user_model()]:
    user = get_user_model().objects.get(username=username)
    following = Follow.objects.filter(follower=user)
    return following