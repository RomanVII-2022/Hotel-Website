from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegistrationForm, ChangePasswordForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
class RegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_message = "Your account was created successfully"
    success_url = reverse_lazy('register')


class PasswordChangeView(PasswordChangeView):
    model = User
    form_class = ChangePasswordForm
    template_name = 'registration/passwordchange.html'
    success_url = reverse_lazy('passwordchange')

