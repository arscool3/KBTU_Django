# Generated by Django 5.0.3 on 2024-03-09 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_purchase_cost_alter_userinfo_default_adress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='default_adress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Store.adress'),
        ),
    ]
