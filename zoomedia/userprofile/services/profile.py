from ..models import Follow , Profile
from django.db.models import QuerySet
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from ..selectors.profile import *

def create_profile(*,user:get_user_model() , bio:str | None ) -> Profile:
    return Profile.objects.create(user=user , bio=bio)


def profile_info_update():
    profiles =  cache.keys("profile_*")
    for key in profiles:
        username = key.replace("profile_" , "")
        data = cache.get(key)
        try:
           profile = Profile.objects.get(user__username=username)
           profile.follower_count = data.get("follower_count")
           profile.following_count = data.get("following_count")
           profile.save()    
        except ObjectDoesNotExist as ex:
            print (f"{ex}")
        except Exception as ex :
            print(f"An error occured : Detail -> {ex}")

def cache_profile(*,user:get_user_model()):
    profile = {
        "follower_count": get_followers(user=user),
        "following_count": get_following(user=user)
    }
    cache.set(f'profile_{user}', profile, timeout=None )
