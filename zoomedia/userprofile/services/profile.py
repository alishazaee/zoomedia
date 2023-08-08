from ..models import Follow , Profile
from django.db.models import QuerySet
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from ..selectors.profile import *

def create_profile(*,username:str , bio:str | None ) -> Profile:
    user = get_user_model().objects.get(username=username)
    return Profile.objects.create(user=user , bio=bio)

def update_profile(*,username:str , bio:str | None ) -> Profile:
    user = get_user_model().objects.get(username=username)
    profile = Profile.objects.get(user=user)
    profile.bio = bio
    profile.save()
    return profile

def profile_info_from_cache_to_db():
    profiles =  cache.keys("profile_*")
    for key in profiles:
        username = key.replace("profile_" , "")
        data = cache.get(key)
        try:
           profile = Profile.objects.get(user__username=username)
           profile.follower_count = data.get("follower_count")
           profile.following_count = data.get("following_count")
           profile.post_counts = data.get("post_counts")

           profile.save()    
        except ObjectDoesNotExist as ex:
            print (f"{ex}")
        except Exception as ex :
            print(f"An error occured : Detail -> {ex}")

def cache_profile(*,user:get_user_model()):
    profile = {
        "follower_count": get_follower_count(user=user),
        "following_count": get_following_count(user=user),
        "post_counts" : get_post_count(user=user)
    }
    cache.set(f'profile_{user}', profile, timeout=None )
