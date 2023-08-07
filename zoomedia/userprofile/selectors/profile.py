from ..models import Follow , Profile
from django.db.models import QuerySet
from django.contrib.auth import get_user_model

def get_followers(*, user: get_user_model())-> int:
    return Follow.objects.filter(following=user).count()

def get_following(*, user:get_user_model()) -> int:
    return Follow.objects.filter(follower=user).count()

def get_profile_detail(*,user:get_user_model()) -> Profile:
    return Profile.objects.get(user__username=user.username)