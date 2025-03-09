from django.urls import path
from .views import (
    home_view,
    about_view,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', home_view, name='home'),  # Home view
    path('about/', about_view, name='about'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]