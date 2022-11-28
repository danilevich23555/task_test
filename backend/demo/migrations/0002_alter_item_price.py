# Generated by Django 4.1.3 on 2022-11-24 08:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=18, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]