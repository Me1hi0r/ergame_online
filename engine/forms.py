from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'secret_key']