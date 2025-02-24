from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models

# Create your models here.

def validator_name(value):
    if len(value) <= 7:
        raise ValidationError(
            "name is too short :("
        )

class Todo(models.Model):
    name = models.CharField(max_length=128 , default="Unnamed Task" , validators=[validator_name])
    checked = models.BooleanField(default=False)
    due_date = models.DateField(default="2000-01-01")

    def get_url(self):
        return f"/update/{self.id}/"

    def get_url_delete(self):
        return f"/delete/{self.id}/"

    class Meta:
        verbose_name = "Todo"

