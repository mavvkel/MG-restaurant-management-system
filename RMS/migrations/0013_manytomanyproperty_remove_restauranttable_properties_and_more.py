# Generated by Django 4.1.7 on 2023-06-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0012_alter_restauranttable_properties'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManyToManyProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='restauranttable',
            name='properties',
        ),
        migrations.AddField(
            model_name='restauranttable',
            name='properties',
            field=models.ManyToManyField(to='RMS.manytomanyproperty'),
        ),
    ]