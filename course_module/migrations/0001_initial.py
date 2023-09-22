# Generated by Django 4.2.5 on 2023-09-22 13:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "course_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("course_name", models.CharField(max_length=255, unique=True)),
                ("course_code", models.CharField(max_length=255, unique=True)),
                ("course_description", models.TextField()),
                ("course_credit", models.IntegerField()),
                ("course_duration", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
