from django.urls import path, include

urlpatterns = [
     path('zoomedia/users/', include(('zoomedia.users.urls', 'users')) , name='users'),
     path('zoomedia/auth/', include(('zoomedia.authentication.urls' , 'auth')) , name='auth')
]
