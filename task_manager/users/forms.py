from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2']


class UserEditForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2']
