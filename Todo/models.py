from django.core.exceptions import ValidationError
from django.db import models
from datetime import date

# Custom validator
def validator_name(value):
    print(f"validating {value}")
    if len(value) <= 7:
        raise ValidationError("Name is too short :(")

class Todo(models.Model):
    name = models.CharField(
        max_length=128,
        default="Unnamed Task",
        validators=[validator_name],
        error_messages={'validators': "Name is too short"}
    )
    checked = models.BooleanField(default=False)
    due_date = models.DateField(default=date.today)

    class Meta:
        verbose_name = "Todo"
