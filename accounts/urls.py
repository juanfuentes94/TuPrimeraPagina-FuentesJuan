"""
accounts/urls.py
"""

from django.urls import path
from .views import (
    register_view,
    CustomLoginView,
    CustomLogoutView,
    profile_view,
    profile_edit_view,
    CustomPasswordChangeView
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]
