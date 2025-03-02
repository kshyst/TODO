from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from Todo.models import Todo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["name", "due_date", "checked"]

    name = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "id": "taskInput",
                "placeholder": "Add a new task!!!",
            }
        ),
    )

    due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "type": "date",
                "id": "dueDateInput",
            }
        )
    )

    checked = forms.BooleanField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "type": "checkbox",
            }
        ),
    )


def search_validation(value):
    if len(value) < 3:
        raise ValidationError(message="Search Query Must Be Longer Than 3 Characters")


class SearchForm(forms.Form):
    class Meta:
        fields = ["search_text"]

    search_text = forms.CharField(
        max_length=128,
        required=False,
        validators=[search_validation],
        widget=forms.TextInput(
            attrs={
                "type": "search",
            }
        ),
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        max_length=128,
        widget=forms.TextInput(attrs={"type": "text"}),
    )

    password1 = forms.CharField(
        required=True,
        max_length=128,
        widget=forms.PasswordInput(attrs={"type": "password"}),
    )

    email = forms.EmailField(
        required=True,
        max_length=128,
        validators=[EmailValidator],
        widget=forms.EmailInput(attrs={"type": "email"}),
    )

    password2 = None

    class Meta:
        model = User
        fields = ["username", "email", "password1"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
