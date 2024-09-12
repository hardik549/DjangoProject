# Generated by Django 5.1.1 on 2024-09-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserDetails",
            fields=[
                (
                    "username",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(blank=True, max_length=12)),
            ],
        ),
    ]
