
from ..models import Follow , Profile
from django.db.models import QuerySet
from django.contrib.auth import get_user_model
from django.core.cache import cache
from ..selectors.profile import *
def cache_profile(*,user:get_user_model()):
    profile = {
        "follower_count": get_followers(user=user),
        "following_count": get_following(user=user)
    }
    cache.set(f'profile_{user}', profile, timeout=None , version='')


def create_follow(* , src_user: get_user_model() , target_username: str  ) -> get_user_model():
    user = get_user_model().objects.get(username=target_username)
    follow = Follow(follower=src_user, following=user)
    follow.full_clean()
    follow.save()
    cache_profile(user=follow.follower)
    cache_profile(user=follow.following)
    return follow.following


def delete_follow(* , src_user: get_user_model() , target_username:str  ) -> None:
    user = get_user_model().objects.get(username=target_username)
    Follow.objects.filter(follower=src_user, following=user).delete()
    cache_profile(user=user)
    cache_profile(user=src_user)


