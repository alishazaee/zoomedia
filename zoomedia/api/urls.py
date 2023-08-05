from django.urls import path, include

urlpatterns = [
     path('users/', include(('zoomedia.users.urls', 'users')) , 'users'),
     path('auth/', include(('zoomedia.authentication.urls')) , 'auth')
]
