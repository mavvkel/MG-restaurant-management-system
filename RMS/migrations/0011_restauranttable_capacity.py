# Generated by Django 4.1.7 on 2023-05-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0010_restauranttable'),
    ]

    operations = [
        migrations.AddField(
            model_name='restauranttable',
            name='capacity',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
