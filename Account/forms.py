from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# i don't actually really know why using this instead of just creating a model


class CreateUSerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
