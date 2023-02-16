from django.urls import include, path
from .views import LoginView, LogoutView, UserCreateView, ProfileCreateView, UserDeleteView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/register/', UserCreateView.as_view(), name='register'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]