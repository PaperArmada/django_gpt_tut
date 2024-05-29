from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_retrieve_update_destroy'),
    path('auth/', obtain_auth_token, name='api_token_auth'),
]