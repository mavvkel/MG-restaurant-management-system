# Generated by Django 4.1.7 on 2023-05-18 09:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0007_restaurantmenuentry_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishrestaurantmenuentry',
            name='restaurantmenuentry_ptr',
        ),
        migrations.RemoveField(
            model_name='drinkrestaurantmenuentry',
            name='restaurantmenuentry_ptr',
        ),
        migrations.AddField(
            model_name='dishrestaurantmenuentry',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dishrestaurantmenuentry',
            name='name',
            field=models.CharField(default=1, max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Name must be at least 2 characters long.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dishrestaurantmenuentry',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.25, max_digits=19, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='Price cannot be negative.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drinkrestaurantmenuentry',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drinkrestaurantmenuentry',
            name='name',
            field=models.CharField(default=1, max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Name must be at least 2 characters long.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drinkrestaurantmenuentry',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=19, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='Price cannot be negative.')]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='RestaurantMenuEntry',
        ),
    ]