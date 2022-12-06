from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username=forms.CharField(max_length=63, label='Matricule')
    password=forms.CharField(max_length=63,widget=forms.PasswordInput,label='Mot de passe')


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','email','password1','password2']
