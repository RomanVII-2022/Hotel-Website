from cProfile import label
from dataclasses import fields
from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your first name'}), label='')
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your last name'}), label='')
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your username'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your email'}), label='')
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your password'}), label='')
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Confirm your password'}), label='')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    
    username = UsernameField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your username'}), label='')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your password'}), label='')

    class Meta:
        fields = ('username', 'password')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your old password'}), label='')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Enter your new password'}), label='')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control bg-transparent p-4 font-weight-bold', 'placeholder':'Confirm your new password'}), label='')
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')