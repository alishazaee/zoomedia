from celery import shared_task
from .services.profile import profile_info_update

@shared_task
def profile_info_update():
    profile_info_update()
    