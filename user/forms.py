from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'phone', 'email', 'password1', 'password2', 'company_name', 'work_field')

