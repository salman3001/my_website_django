from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "web"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout_confirm/", views.LogoutConfirm.as_view(), name="logout_confirm"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("password-change/", views.PasswordChange.as_view(), name="password-change"),
    path(
        "password-change-done/",
        views.PasswordChangeDone.as_view(),
        name="password-change-done",
    ),
    path("password-reset/", views.PasswordReset.as_view(), name="password-reset"),
    path(
        "password-reset-done/",
        views.PasswordResetDone.as_view(),
        name="password-reset-done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        views.PasswordResetConfirm.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "password-reset-complete/",
        views.PasswordResetComplete.as_view(),
        name="password-reset-complete",
    ),
]
