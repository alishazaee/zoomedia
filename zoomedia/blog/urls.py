from django.urls import path
from .apis.post import PostApi , PostDetailApi , FeedApi


urlpatterns = [
    path('posts/', PostApi.as_view(),name="posts"),
    path('post/<str:slug>', PostDetailApi.as_view(),name="post"),
    path('feed/', FeedApi.as_view(),name="feed"),


]
