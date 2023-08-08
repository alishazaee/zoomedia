from django.urls import path
from .apis.post import PostApi , PostDetailApi


urlpatterns = [
    path('posts/', PostApi.as_view(),name="posts"),
    path('post/<str:slug>', PostDetailApi.as_view(),name="post"),


]
