from django.db import transaction 
from .models import BaseUser
from .tasks import create_profile_for_new_user

def create_user(*, email:str, password:str , username:str) -> BaseUser:
    newuser= BaseUser.objects.create_user(email=email, password=password , username=username)
    create_profile_for_new_user.delay(username=newuser.username)
    return newuser