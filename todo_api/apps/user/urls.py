from django.urls import path
from .views import UserSignUpView, LoginView, logout_view

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name='user_signup'),
    path("login/", LoginView.as_view(), name='user_login'),
    path("logout/", logout_view, name='user_logout'),
]