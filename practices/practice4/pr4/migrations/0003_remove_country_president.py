# Generated by Django 4.1.7 on 2024-02-25 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pr4', '0002_remove_country_capital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='president',
        ),
    ]