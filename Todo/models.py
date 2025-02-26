from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


def validator_name(value):
    if len(value) <= 7:
        raise ValidationError("name is too short :(")


class Todo(models.Model):
    name = models.CharField(
        max_length=128, default="Unnamed Task", validators=[validator_name]
    )
    checked = models.BooleanField(default=False)
    due_date = models.DateField(default="2000-01-01")

    class Meta:
        verbose_name = "Todo"
