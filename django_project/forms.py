from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    #username = forms.CharField(max_length=150, required=True, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #last_name = forms.CharField(max_length=30, required=False, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

