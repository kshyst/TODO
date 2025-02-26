from django import forms
from django.core.exceptions import ValidationError

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
