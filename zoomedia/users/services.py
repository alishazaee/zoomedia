from django.db import transaction 
from .models import BaseUser



def create_user(*, email:str, password:str , username:str) -> BaseUser:
    return BaseUser.objects.create_user(email=email, password=password , username=username)
