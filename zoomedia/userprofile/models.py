from django.db import models
from zoomedia.common.models import BaseModel
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class Profile(BaseModel):
    user= models.ForeignKey(get_user_model(), on_delete=models.CASCADE ,related_name='user')
    following_count= models.PositiveBigIntegerField(default=0)
    follower_count = models.PositiveBigIntegerField(default=0)
    bio = models.CharField(max_length=255 , null=True, blank=True)
    post_counts = models.PositiveIntegerField(default=0)
class Follow(BaseModel):
    follower=models.ForeignKey(get_user_model(), on_delete=models.CASCADE ,related_name='follower')
    following=models.ForeignKey(get_user_model(), on_delete=models.CASCADE ,related_name='following')
    
    class Meta:
        unique_together = ('follower', 'following')
    
    def clean(self):
        if self.follower == self.following:
            raise ValidationError("You can not follow yourself")
    