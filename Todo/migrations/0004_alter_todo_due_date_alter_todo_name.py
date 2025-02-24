# Generated by Django 4.2.19 on 2025-02-24 13:54

import Todo.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_alter_todo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(default='Unnamed Task', error_messages={'validators': 'Name is too short'}, max_length=128, validators=[Todo.models.validator_name]),
        ),
    ]
