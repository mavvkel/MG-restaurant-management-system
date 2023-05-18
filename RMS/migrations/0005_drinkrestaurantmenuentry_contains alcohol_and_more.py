# Generated by Django 4.1.7 on 2023-04-11 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0004_alter_dishrestaurantmenuentry_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkrestaurantmenuentry',
            name='Contains alcohol',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='drinkrestaurantmenuentry',
            name='volume',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=19, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='Volume cannot be negative.')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='chatId',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(limit_value=6, message='ID should be at least 6 characters long.')]),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Enter valid phone number.', regex='^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$')]),
        ),
        migrations.AlterField(
            model_name='dishrestaurantmenuentry',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Name must be at least 2 characters long.')]),
        ),
        migrations.AlterField(
            model_name='dishrestaurantmenuentry',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Price cannot be negative.')]),
        ),
        migrations.AlterField(
            model_name='dishrestaurantmenuentry',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=19, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='Weight cannot be negative.')]),
        ),
        migrations.AlterField(
            model_name='drinkrestaurantmenuentry',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Name must be at least 2 characters long.')]),
        ),
        migrations.AlterField(
            model_name='drinkrestaurantmenuentry',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Price cannot be negative.')]),
        ),
    ]