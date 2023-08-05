from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.conf import settings
from ..models import Follow
@receiver(pre_delete , sender=settings.AUTH_USER_MODEL )
def delete_following(sender,instance , **kwargs):
    # Delete the followings of the delete user
    Follow.objects.filter(following=instance).delete()
    # Delete the followers of the deleted user
    Follow.objects.filter(follower=instance).delete()
    