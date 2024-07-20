# accounts/views.py
from django.shortcuts import redirect

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from .forms import SignUpForm


class LoginView(LoginView):
    template_name = "accounts/login.html"


class LogoutView(LogoutView):
    template_name = "accounts/logged_out.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy(
        "accounts:login"
    )  # Redirect to the login page after successful registration
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
