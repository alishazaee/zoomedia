from ..models import Follow , Profile
from django.db.models import QuerySet
from django.contrib.auth import get_user_model

def create_profile(*,user:get_user_model() , bio:str | None ) -> Profile:
    return Profile.objects.create(user=user , bio=bio)