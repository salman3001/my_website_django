from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordResetForm

# Create your views here.


def home(request):
    return render(request, "web/home.html")


def about(request):
    return render(request, "web/about.html")


class Login(LoginView):
    next_page = reverse_lazy("web:home")
    template_name = "web/login.html"


class Logout(LogoutView):
    next_page = reverse_lazy("web:login")


class LogoutConfirm(TemplateView):
    template_name = "web/logout_confirm.html"


@method_decorator(login_required(login_url=reverse_lazy("web:login")), name="dispatch")
class PasswordChange(PasswordChangeView):
    template_name = "web/password_change.html"
    success_url = reverse_lazy("web:password-change-done")


class PasswordChangeDone(TemplateView):
    template_name = "web/password_change_done.html"


class PasswordReset(PasswordResetView):
    template_name = "web/password_reset_form.html"
    success_url = reverse_lazy("web:password_reset_done")


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "web/password_reset_confirm.html"


class PasswordResetDone(TemplateView):
    template_name = "web/password_reset_done.html"
