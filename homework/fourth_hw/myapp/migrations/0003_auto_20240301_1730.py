# Generated by Django 3.2.18 on 2024-03-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20240301_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='genre',
            name='books',
            field=models.ManyToManyField(to='myapp.Book'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='books',
            field=models.ManyToManyField(to='myapp.Book'),
        ),
    ]
