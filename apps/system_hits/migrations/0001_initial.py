# Generated by Django 4.1.2 on 2022-11-27 20:08

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=100)),
                ("objetive_name", models.CharField(max_length=100)),
                ("state", django_fsm.FSMField(default="active", max_length=50)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]
