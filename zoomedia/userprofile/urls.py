from django.urls import path
from .apis.Follow import FollowApi
from .apis.Profile import ProfileApi


urlpatterns = [
    path('account/', ProfileApi.as_view(),name="account"),
    path('follow/<str:username>', FollowApi.as_view(),name="follow"),

]
