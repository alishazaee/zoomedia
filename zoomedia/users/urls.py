from django.urls import path
from .apis import UserApi


urlpatterns = [
    path('', UserApi.as_view(),name=""),
]
