from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=128 , default="Unnamed Task")
    checked = models.BooleanField(default=False)
    due_date = models.DateField(default="2000-01-01")

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todo List"