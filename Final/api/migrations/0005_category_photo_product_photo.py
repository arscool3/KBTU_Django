# Generated by Django 4.2 on 2023-04-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product_small_descr'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
