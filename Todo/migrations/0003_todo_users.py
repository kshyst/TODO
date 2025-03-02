# Generated by Django 4.2.19 on 2025-03-01 08:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Todo", "0002_delete_todouser"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
