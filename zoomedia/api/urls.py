from django.urls import path, include

urlpatterns = [
     path('zoomedia/users/', include(('zoomedia.users.urls', 'users')) , name='users'),
     path('zoomedia/auth/', include(('zoomedia.authentication.urls' , 'auth')) , name='auth'),
     path('zoomedia/profile/', include(('zoomedia.userprofile.urls' , 'profile')) , name='profile'),
     path('zoomedia/blog/', include(('zoomedia.blog.urls' , 'blog')) , name='blog')

]
