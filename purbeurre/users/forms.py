from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput, TextInput
from django.utils.translation import gettext_lazy as _

from .models import User

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email"]
