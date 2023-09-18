# Generated by Django 4.2.5 on 2023-09-17 17:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("course_module", "0002_alter_course_department_alter_course_teacher"),
        ("school_module", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseMaterial",
            fields=[
                (
                    "course_material_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("course_material_name", models.CharField(max_length=255)),
                (
                    "course_material_file",
                    models.FileField(upload_to="course_materials"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course_module.course",
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school_module.school",
                    ),
                ),
            ],
        ),
    ]
