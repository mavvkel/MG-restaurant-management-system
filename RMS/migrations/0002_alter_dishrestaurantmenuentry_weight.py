# Generated by Django 4.1.7 on 2023-04-11 16:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishrestaurantmenuentry',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=19, validators=[django.core.validators.MinValueValidator(0.0, 'Weight cannot be negative.')]),
        ),
    ]
