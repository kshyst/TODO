# Generated by Django 4.2.19 on 2025-02-25 07:49

import Todo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_alter_todo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(default='Unnamed Task', max_length=128, validators=[Todo.models.validator_name]),
        ),
    ]
