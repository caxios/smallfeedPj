from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    school = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'school', 'email', 'password1', 'password2']