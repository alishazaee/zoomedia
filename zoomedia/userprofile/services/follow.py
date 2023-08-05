
from ..models import Follow , Profile
from django.db.models import QuerySet
from django.contrib.auth import get_user_model

def create_follow(* , src_user: get_user_model() , target_username: str  ) -> get_user_model():
    user = get_user_model().objects.get(username=target_username)
    follow = Follow(follower=src_user, following=user)
    follow.full_clean()
    follow.save()
    return follow.following


def delete_follow(* , src_user: get_user_model() , target_username:str  ) -> None:
    user = get_user_model().objects.get(username=target_username)
    Follow.objects.filter(follower=src_user, following=user).delete()
    

