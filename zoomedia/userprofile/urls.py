from django.urls import path
from .apis.Follow import FollowApi , FollowerApi , FollowingApi
from .apis.Profile import ProfileApi


urlpatterns = [
    path('account/', ProfileApi.as_view(),name="account"),
    path('follow/<str:username>', FollowApi.as_view(),name="follow"),
    path('follower/', FollowerApi.as_view(),name="follower"),
    path('following/', FollowingApi.as_view(),name="following"),


]
