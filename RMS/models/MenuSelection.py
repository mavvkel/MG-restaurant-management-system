from django.db import models
from django.apps import apps


class MenuSelection(models.Model):
    order = models.ForeignKey('RMS.RestaurantOrder', on_delete=models.CASCADE)
    menu_entry = models.ForeignKey('RMS.RestaurantMenuEntry', on_delete=models.CASCADE)
    # order = apps.get_model('RMS.RestaurantOrder')
    # menu_entry = apps.get_model('RMS.RestaurantMenuEntry')
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.count
