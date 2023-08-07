from celery import shared_task
from zoomedia.userprofile.services.profile import create_profile
from django.contrib.auth import get_user_model
@shared_task
def create_profile_for_new_user(* , username : str):
    create_profile(username=username , bio=None)
    