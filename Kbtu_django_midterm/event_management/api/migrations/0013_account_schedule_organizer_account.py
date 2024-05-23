# Generated by Django 4.1.7 on 2024-03-11 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
            ],
        ),
        migrations.AddField(
            model_name='organizer',
            name='account',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.account'),
            preserve_default=False,
        ),
    ]
