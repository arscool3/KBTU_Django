# Generated by Django 4.2.11 on 2024-03-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_gym_member_workout_membership_equipment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name': 'instructor'},
        ),
        migrations.AddField(
            model_name='gym',
            name='gym_name',
            field=models.CharField(default='Default', max_length=100),
            preserve_default=False,
        ),
    ]