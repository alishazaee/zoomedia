from celery import shared_task
from .services.profile import profile_info_from_cache_to_db

@shared_task
def profile_info_update_task():
    profile_info_from_cache_to_db()
    