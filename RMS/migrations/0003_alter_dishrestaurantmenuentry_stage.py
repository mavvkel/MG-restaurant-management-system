# Generated by Django 4.1.7 on 2023-04-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0002_alter_dishrestaurantmenuentry_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishrestaurantmenuentry',
            name='stage',
            field=models.IntegerField(choices=[(1, 'Starter'), (2, 'Main course'), (3, 'Soup'), (4, 'Salad'), (5, 'Dessert')]),
        ),
    ]
