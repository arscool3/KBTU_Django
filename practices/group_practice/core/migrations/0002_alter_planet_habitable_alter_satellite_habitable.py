# Generated by Django 4.2.4 on 2024-02-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='habitable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='habitable',
            field=models.BooleanField(default=False),
        ),
    ]
