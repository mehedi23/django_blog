from django.urls import path, include
from account.views.Auth import RegistrationView, LoginView, TokenRefreshView
from account.views.UserInfo import UserView


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('profile/', UserView.as_view(), name='profile'),
]