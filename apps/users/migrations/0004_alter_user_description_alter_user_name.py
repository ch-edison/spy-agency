# Generated by Django 4.1.2 on 2022-11-30 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="description",
            field=models.CharField(
                blank=True, max_length=120, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, max_length=100, verbose_name="Name"),
        ),
    ]
