# Generated by Django 5.0.3 on 2024-03-10 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_commentary_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
    ]
