from django.db import models
from zoomedia.common.models import BaseModel
from django.conf import settings
from django.core.exceptions import ValidationError
class Profile(BaseModel):
    user= models.ForeignKey(settings.AUTH_USER, on_delete=models.CASCADE ,related_name='user')
    following_count= models.PositiveBigIntegerField(default=0)
    follower_count = models.PositiveBigIntegerField(default=0)

class Follow(BaseModel):
    follower=models.ForeignKey(settings.AUTH_USER, on_delete=models.CASCADE ,related_name='follower')
    following=models.ForeignKey(settings.AUTH_USER, on_delete=models.CASCADE ,related_name='following')
    class Meta:
        unique_together = ('follower', 'following')
    
    def clean(self):
        if self.src_user == self.target_user:
            raise ValidationError("You can not follow yourself")
    