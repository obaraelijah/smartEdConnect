# Generated by Django 4.2.5 on 2023-09-15 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0010_alter_customuser_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="accounts.role"
            ),
        ),
    ]
