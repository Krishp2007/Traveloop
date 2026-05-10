from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import StyledLoginForm
from . import views_auth

urlpatterns = [
    path("signup/", views_auth.sign_up, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="travel/auth/login.html",
            form_class=StyledLoginForm,
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="travel/auth/password_reset.html",
            email_template_name="travel/auth/password_reset_email.txt",
            success_url="/accounts/password-reset/done/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="travel/auth/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="travel/auth/password_reset_confirm.html",
            success_url="/accounts/reset/done/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="travel/auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
