from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=128 , default="Unnamed Task")
    checked = models.BooleanField(default=False)
    due_date = models.DateField(default="2000-01-01")

    def get_url(self):
        return f"/update/{self.id}/"

    def get_url_delete(self):
        return f"/delete/{self.id}/"

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todo List"