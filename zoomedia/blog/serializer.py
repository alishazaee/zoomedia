from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ( 'username' , )
        
class postserializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    url = serializers.SerializerMethodField("get_url" , read_only=True)
    def get_url(self , post):
        request = self.context.get("request")
        path = reverse("api:blog:post", args=(post.slug,))
        return request.build_absolute_uri(path)


    class Meta:
        model = Post
        fields = ('url' , 'author' , 'title' , 'description')
