# Generated by Django 4.1.13 on 2024-03-11 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="description",
            new_name="about",
        ),
        migrations.RenameField(
            model_name="event",
            old_name="title",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="avatar",
            new_name="profile_photo",
        ),
    ]
