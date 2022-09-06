from django.urls import path
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [
    path('login', views.AuthenticationViewSet.as_view({'post': 'login'}), name='login'),
    path('logout', views.AuthenticationViewSet.as_view({'get': 'logout'}), name='logout'),
    path('register', views.AuthenticationViewSet.as_view({'post': 'register'}), name='register'),
    path('reset-password', views.AuthenticationViewSet.as_view({'patch': 'reset-password'}), name='reset-password'),
    path('authorize-moderator',
         views.AuthenticationViewSet.as_view({'patch': 'authorize-moderator'}), name='authorize-moderator'),
    path('update-profile', views.AuthenticationViewSet.as_view({'patch': 'update-profile'}), name='update-profile'),
    # path('friend')
    # path('unfriend')

    # tokenization
    path('api-token-auth/', auth_views.obtain_auth_token)
]
