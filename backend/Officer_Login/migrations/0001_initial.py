# Generated by Django 5.2.3 on 2025-07-10 06:25

import Officer_Login.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Officer",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=Officer_Login.models.generate_officer_id,
                        editable=False,
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "password",
                    models.CharField(
                        max_length=200,
                        validators=[django.core.validators.MinLengthValidator(8)],
                    ),
                ),
            ],
        ),
    ]
