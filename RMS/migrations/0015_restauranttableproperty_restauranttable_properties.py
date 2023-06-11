# Generated by Django 4.1.7 on 2023-06-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0014_remove_restauranttable_properties_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantTableProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.IntegerField(choices=[(1, 'Near window'), (2, 'Near kitchen'), (3, 'In garden'), (4, 'In bar'), (5, 'Is isolated')])),
            ],
        ),
        migrations.AddField(
            model_name='restauranttable',
            name='properties',
            field=models.ManyToManyField(to='RMS.restauranttableproperty', verbose_name='list of properties'),
        ),
    ]