# Generated by Django 5.0.3 on 2024-03-11 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursera.instructor'),
        ),
    ]