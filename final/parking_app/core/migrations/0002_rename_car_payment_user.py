# Generated by Django 5.0.4 on 2024-05-12 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='car',
            new_name='user',
        ),
    ]
