# Generated by Django 4.1.7 on 2023-05-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0011_restauranttable_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restauranttable',
            name='properties',
            field=models.IntegerField(choices=[(1, 'Near window'), (2, 'Near kitchen'), (3, 'In garden'), (4, 'In bar'), (5, 'Is isolated')]),
        ),
    ]
