# authentication/urls.py

from django.urls import path
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    UserDetailsView,
    PasswordResetView,
    PasswordResetConfirmView
)
from django.urls import path
from .views import *



urlpatterns = [
    path('register', CustomRegisterView.as_view(), name='rest_register'),
    path('send_verification_code', CustomSendVerificationCodeView.as_view(), name='rest_send_verification_code'),
    path('verify_email', CustomVerifyEmailView.as_view(), name='rest_verify_email'),
    path("login", LoginView.as_view(), name="rest_login"),
    path("logout", LogoutView.as_view(), name="rest_logout"),
    path("user", UserDetailsView.as_view(), name="rest_user_details"),
    path("password/reset", PasswordResetView.as_view(), name="rest_password_reset"),
    path("password/reset/confirm/<str:uidb64>/<str:token>", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]


