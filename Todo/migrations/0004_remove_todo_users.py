# Generated by Django 4.2.19 on 2025-03-01 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_todo_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='users',
        ),
    ]
