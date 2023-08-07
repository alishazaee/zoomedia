

from rest_framework import serializers
from .models import Follow , Profile
from django.conf import settings
from django.contrib.auth import get_user_model
from zoomedia.users.models import BaseUser
from django.core.cache import cache

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class get_profile_detail_serializer( serializers.ModelSerializer):
    user= user_serializer(read_only=True)
    follower_count= serializers.CharField(read_only=True)
    following_count= serializers.CharField(read_only=True)
    
    def to_representation(self, instance):
        represent =  super().to_representation(instance)
        cache_profile = cache.get(f"profile_{instance.user}", {})
        if cache_profile:
                represent["posts_count"] = cache_profile.get("posts_count")
                represent["subscriber_count"] = cache_profile.get("subscribers_count")
                represent["subscription_count"] = cache_profile.get("subscriptions_count")

        return represent


    class Meta:
        model = Profile
        fields = ('user' , 'bio' ,'follower_count' , 'following_count')
    
class get_profile_serializer( serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)

