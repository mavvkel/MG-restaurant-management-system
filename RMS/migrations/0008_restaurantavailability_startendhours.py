# Generated by Django 4.1.7 on 2023-05-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0007_restaurant_restauranttable_restaurantworker'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StartEndHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]