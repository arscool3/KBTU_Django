# Generated by Django 4.1.7 on 2024-02-27 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr5.faculty')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr5.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('year', models.IntegerField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr5.faculty')),
                ('lessons', models.ManyToManyField(to='pr5.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
