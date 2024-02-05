from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm

# Create your views here.


class LoginNotRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy("web:home"))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy("web:home"))
        return super().get(request, *args, **kwargs)


def home(request):
    return render(request, "web/home.html")


def about(request):
    return render(request, "web/about.html")


class Login(LoginNotRequiredMixin, LoginView):
    next_page = reverse_lazy("web:home")
    template_name = "registration/login.html"


class Signup(SuccessMessageMixin, LoginNotRequiredMixin, CreateView):
    model = User
    template_name = "registration/signup_form.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("web:login")


class Logout(LogoutView):
    next_page = reverse_lazy("web:login")


class LogoutConfirm(TemplateView):
    template_name = "registration/logout_confirm.html"


@method_decorator(login_required(login_url=reverse_lazy("web:login")), name="dispatch")
class PasswordChange(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("web:password_change_done")


class PasswordChangeDone(TemplateView):
    template_name = "registration/password_change_done.html"


class PasswordReset(PasswordResetView):
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy("web:password_reset_done")
    email_template_name = "registration/password_reset_email.html"


class PasswordResetDone(PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"
    success_url = reverse_lazy("web:password_reset_complete")


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "registration/password_reset_complete.html"
