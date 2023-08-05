

from rest_framework import serializers
from .models import Follow , Profile
from django.conf import settings
from django.contrib.auth import get_user_model
from zoomedia.users.models import BaseUser
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class get_profile_detail_serializer( serializers.ModelSerializer):
    user= user_serializer(read_only=True)
    follower_count= serializers.CharField(read_only=True)
    following_count= serializers.CharField(read_only=True)
    class Meta:
        model = Profile
        fields = ('user' , 'bio' ,'follower_count' , 'following_count')
    
class get_profile_serializer( serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)

class get_follow_detail_serializer( serializers.ModelSerializer):
    user= user_serializer(read_only=True)
    follower_count= serializers.CharField(read_only=True)
    following_count= serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ('user' , 'bio' ,'follower_count' , 'following_count')
    
class get_follow_serializer( serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)
    