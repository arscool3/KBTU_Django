# Generated by Django 4.2 on 2023-04-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank=True)),
                ('password', models.TextField()),
                ('is_admin', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
