# Generated by Django 5.0.1 on 2024-03-29 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Comment', models.CharField(max_length=250)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gist',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.CharField(blank=True, max_length=150, null=True)),
                ('Visible', models.BooleanField(default=False)),
                ('IsForked', models.BooleanField(default=False)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Code', models.TextField()),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
                ('CommitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.commit')),
            ],
        ),
        migrations.AddField(
            model_name='commit',
            name='GistID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.gist'),
        ),
    ]
