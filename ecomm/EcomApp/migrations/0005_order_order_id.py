# Generated by Django 5.0.4 on 2024-04-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
