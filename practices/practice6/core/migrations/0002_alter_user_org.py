# Generated by Django 4.1.7 on 2024-03-11 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='org',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.org'),
        ),
    ]