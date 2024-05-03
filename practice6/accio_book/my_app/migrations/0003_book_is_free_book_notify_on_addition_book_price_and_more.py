# Generated by Django 4.1.7 on 2024-04-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_readingprogress_userprofile_remove_book_publisher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='notify_on_addition',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
