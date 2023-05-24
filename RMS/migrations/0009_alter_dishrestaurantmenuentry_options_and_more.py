# Generated by Django 4.1.7 on 2023-05-23 17:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('RMS', '0008_remove_dishrestaurantmenuentry_restaurantmenuentry_ptr_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishrestaurantmenuentry',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='drinkrestaurantmenuentry',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='dishrestaurantmenuentry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dishrestaurantmenuentry',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dishrestaurantmenuentry',
            name='price',
        ),
        migrations.RemoveField(
            model_name='drinkrestaurantmenuentry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='drinkrestaurantmenuentry',
            name='name',
        ),
        migrations.RemoveField(
            model_name='drinkrestaurantmenuentry',
            name='price',
        ),
        migrations.CreateModel(
            name='RestaurantMenuEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Name must be at least 2 characters long.')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='Price cannot be negative.')])),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.AddField(
            model_name='dishrestaurantmenuentry',
            name='restaurantmenuentry_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RMS.restaurantmenuentry'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drinkrestaurantmenuentry',
            name='restaurantmenuentry_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RMS.restaurantmenuentry'),
            preserve_default=False,
        ),
    ]
