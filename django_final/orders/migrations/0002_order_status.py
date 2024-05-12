# Generated by Django 4.2.5 on 2023-09-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[("Waiting", "Waiting"), ("Completed", "Completed")],
                default="Waiting",
            ),
        ),
    ]
